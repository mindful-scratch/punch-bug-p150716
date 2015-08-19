<?php

//SAKURA Internet
$global_user_name = "user";
$global_password = "password";
$db_name = "hinoqi_particle";	//データベース名

try {
	$dsn = 'mysql:host=***.sakura.ne.jp;dbname=hinoqi_particle';
	$options = array(PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES utf8');
	$dbh = new PDO($dsn, $global_user_name, $global_password, $options);
}
catch (PDOException $e) {
	exit('データベース接続失敗。'.$e->getMessage());
}


?>