<?php
require_once("db_particle.inc");

if ( isset($_GET['p']) === true ){
	if ( is_numeric($_GET['p']) ){
		$num = intval($_GET['p']);
		if ( -1 < $num && $num < 101 ){
			$stmt = $dbh->prepare("INSERT INTO power(val) VALUES(?)");
			$stmt->bindValue(1, $num, PDO::PARAM_INT);
			if ( $stmt->execute() ){
				echo "success: ", $num;
			}
			else{
				echo "failed";
			}
		}
	}
}
$dbh = null;


