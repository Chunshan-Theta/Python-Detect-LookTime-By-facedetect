<?php
$StartDate = isset($_GET["StartDate"])?$_GET["StartDate"]:null;
$EndDate = isset($_GET["EndDate"])?$_GET["EndDate"]:null;
$StartTime = isset($_GET["StartTime"])?$_GET["StartTime"]:null;
$EndTime = isset($_GET["EndTime"])?$_GET["EndTime"]:null;



function Search_mysqlQuery($sql) {
	/* Connect to a MySQL database using driver invocation */
	$dbname='pi';
	$hostIP='140.130.36.221';
	$user = 'theta';
	$password = 'theta';
	
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


$sql = "SELECT * FROM `peopleattentiononpi` WHERE `Time` >= '".$StartDate." ".$StartTime."' AND `Time` <= '".$EndDate."  ".$EndTime."';";
//print_r( json_encode(Search_mysqlQuery($sql)));
//print_r(Search_mysqlQuery($sql));

$ArraySQLQuery = json_decode(json_encode(Search_mysqlQuery($sql)), True);
//print_r($ArraySQLQuery[0]['Time']);
//print_r($ArraySQLQuery[1]['Time']);
//print_r(strtotime($ArraySQLQuery[20]['Time'])-strtotime($ArraySQLQuery[0]['Time']));
if ($ArraySQLQuery ==[]){
	echo "not Found";
	
}
else{
	$StartTime = $ArraySQLQuery[0]['Time'];
	$EndTime = $ArraySQLQuery[count($ArraySQLQuery)-1]['Time'];
	$DDTime =strtotime($EndTime)-strtotime($StartTime);
	$PeopleStream = Array();
	$FPeopleStream = Array();
	$PeopleNum=0;
	$SumFace=0;
	$SumAttention=0;
	$AverageAttention=0;
	foreach ($ArraySQLQuery as $i){
		Array_push($PeopleStream,$i['PeopleNum']);
	}

	Array_push($FPeopleStream,(int)$ArraySQLQuery[0]['PeopleNum']);
	for($i=1;$i<count($ArraySQLQuery)-1;$i++){
		$Num = ceil(($ArraySQLQuery[($i-1)]['PeopleNum']+$ArraySQLQuery[($i+1)]['PeopleNum']+$ArraySQLQuery[$i]['PeopleNum'])/3);
		Array_push($FPeopleStream,$Num);
	}
	Array_push($FPeopleStream,(int)$ArraySQLQuery[count($ArraySQLQuery)-1]['PeopleNum']);

	for ($i=1;$i<count($FPeopleStream)-1;$i++){
		//$PeopleNum+=abs($ArraySQLQuery[$i]['PeopleNum']-ArraySQLQuery[$i-1]['PeopleNum']);
		$PeopleNum+=abs($FPeopleStream[$i]-$FPeopleStream[$i-1]);
	}
	$PeopleNum = round($PeopleNum/2);
	foreach ($ArraySQLQuery as $i){
		$SumFace+=$i['PeopleNum'];
	}

	$SumAttention=(int)($SumFace*$DDTime/count($ArraySQLQuery));
	$AverageAttention=(float)($SumAttention/$PeopleNum);

/* 	echo "開始時間: ";
	echo $StartTime;
	echo "<br>";

	echo "結束時間: ";
	echo $EndTime;
	echo "<br>";


	echo "預估人數: ";
	echo $PeopleNum;
	echo "<br>";

	echo "總臉數: ";
	echo $SumFace;
	echo "<br>";

	echo "總注視時間: ";
	echo $SumAttention;
	echo "<br>";

	echo "預估平均注視時間: ";
	echo $AverageAttention; 
*/
	
	$result = array(
		"StartTime"=>$StartTime,
		"EndTime"=>$EndTime,
		"PeopleNum"=>$PeopleNum,
		"SumFace"=>$SumFace,
		"SumAttention"=>$SumAttention,
		"AverageAttention"=>$AverageAttention,
		"FPeopleStream"=>$FPeopleStream,
	);
/* 	Array_push($result,$StartTime);
	Array_push($result,$EndTime);
	Array_push($result,$PeopleNum);
	Array_push($result,$SumFace);
	Array_push($result,$SumAttention);
	Array_push($result,$AverageAttention);
	Array_push($result,$FPeopleStream); */
	
	print_r(json_encode($result));
}

?>
