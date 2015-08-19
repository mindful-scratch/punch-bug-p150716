# メイン表示用URL

まず次のメインページにアクセスしてください。

http://hinoqi.sakura.ne.jp/particle/

アクセスすると、パーティクルが表示され、ブラウザ（JavaScript）ローカル内に「表示した日時」が記録されます。

このページの「表示日時」以降に、更新用ページ（後述）の、push.php?p=99 などと投げられた値の、最新値がパーティクルで反映・表示されることになります。

この表示用ページは、Ajaxで、100ms おきに更新がないか見に行きます。現在値と同じであっても、見た目は変わりませんが、一応内部処理的には、毎回更新をかけてます。ただ、内部のintを書き換えているだけですので、さほど問題はありません。

とはいえ、パーティクルの動きに加え、100msのポーリングは、ブラウザに、かなり負荷がかかります。

たぶん動かすPCは、バッテリーを食い、相当ファンが回ると思います。わりと高めのスペックのPC準備と、AC電源をお忘れなく(笑)。

さすがのMacBook Airでも、一時間ばかし作業したら、バッテリー半分くらいになりました。


【更新用URL】
http://hinoqi.sakura.ne.jp/particle/push.php

上記URLへGETで、0〜100 の値を投げます。それ以外の値、文字列やバイナリ、範囲外の数値は捨てられます。

こんな感じで投げてください。引数は「p」です。
http://hinoqi.sakura.ne.jp/particle/push.php?p=99

一応、DBつくって格納してありますが、テーブルは小さいですし、インデックスチューニングもされているので、それほど負荷や遅延は生じない（はず）。

データベースの構成は、以下テキトーな感じ。日時にインデックス張ってます。
```sql
DROP TABLE hinoqi_particle.power;

CREATE TABLE hinoqi_particle.power(
	id INT AUTO_INCREMENT UNIQUE, 
	dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
	val INT, 
	done BOOLEAN DEFAULT FALSE);

CREATE INDEX datetime_index ON hinoqi_particle.power(dt);
```

## 捕捉
一応、前にあった、左クリックで「＋１０」、右クリックで「０リセット」は残してあります。いざというときは、手動でリセットかけたりもできます。


以上
