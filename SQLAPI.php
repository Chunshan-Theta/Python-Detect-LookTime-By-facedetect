<?php

$Token = isset($_POST["Token"])?$_POST["Token"]:null;
$action = isset($_POST["action"])?$_POST["action"]:null;
$PeopleNum = isset($_POST["PeopleNum"])?$_POST["PeopleNum"]:null;
$Time = isset($_POST["Time"])?$_POST["Time"]:null;
$StartTime = isset($_POST["StartTime"])?$_POST["StartTime"]:null;
$EndTime = isset($_POST["EndTime"])?$_POST["EndTime"]:null;

$sql = "INSERT INTO `peopleattentiononpi` (`id`, `PeopleNum`, `Time`) VALUES (NULL, '".$PeopleNum."','".$Time."');";

if($action=='InsertSql'){
	//INSERT INTO `peopleattentiononpi` (`id`, `PeopleNum`, `Time`) VALUES (NULL, '0','2016-09-10 00:00:00');
	$sql = "INSERT INTO `peopleattentiononpi` (`id`, `PeopleNum`, `Time`) VALUES (NULL, '".$PeopleNum."','".$Time."');";
	Insert_mysqlQuery($sql);
	
	
	// test query:http://140.130.36.221/pi/SQLAPI.php?action=InsertSql&PeopleNum=0&Time=2016-09-10%2000:00:00
}
if($action=='SearchSql'){	
	//$sql = "SELECT * FROM `peopleattentiononpi` WHERE `Time` <= '2016-09-10 00:00:00' AND `Time` >= '2016-09-10 00:00:00';";
	$sql = "SELECT * FROM `peopleattentiononpi` WHERE `Time` >= '".$StartTime."' AND `Time` <= '".$EndTime."';";
	print_r( json_encode(Search_mysqlQuery($sql)));
	
	//test query http://140.130.36.221/pi/SQLAPI.php?action=SearchSql&StartTime=2016-09-10%2000:00:00&EndTime=2016-09-10%2010:00:00
}




function Insert_mysqlQuery($sql) {
	/* Connect to a MySQL database using driver invocation */
	$dbname='';
	$hostIP='';
	$user = '';
	$password = '';
	
	$dsn = 'mysql:dbname='.$dbname.';host='.$hostIP;
	try {
		$dbh = new PDO($dsn, $user, $password);
		$dbh->query($sql);	
	} catch (PDOException $e) {
		echo 'Connection failed: '.$e->getMessage();
	}
	
}


function Search_mysqlQuery($sql) {
	/* Connect to a MySQL database using driver invocation */
	$dbname='';
	$hostIP='';
	$user = '';
	$password = '';
	
	$dsn = 'mysql:dbname='.$dbname.';host='.$hostIP;
    $result = null;
	try {
		$dbh = new PDO($dsn, $user, $password);
		$result = $dbh->query($sql)->fetchAll(PDO::FETCH_OBJ);	
	} catch (PDOException $e) {
		echo 'Connection failed: '.$e->getMessage();
	}
	return $result;
}



?>
