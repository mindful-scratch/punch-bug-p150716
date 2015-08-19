<?php
require_once("db_particle.inc");

if (isset($_GET["date"])){
  $start_time = $_GET["date"];
}
else{
  echo "error: 1";
  return;
}

$stmt = $dbh->prepare("SELECT val FROM power WHERE dt > FROM_UNIXTIME(?) ORDER BY dt DESC LIMIT 1;");
$stmt->bindValue(1, $start_time, PDO::PARAM_INT);
$stmt->execute();
$val = "";
while($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
  $val = $row["val"];
}
if ( isset($val) ){
  echo $val;
}
else{
  echo "error: 2";
}

