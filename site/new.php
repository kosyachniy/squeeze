<?php
include('func.php');
$db=db();
header('location: ./');
$cont=preg_replace("/\s{2,}/",' ',preg_replace('/[\r\n]{1,}/s',' ',$_POST['cont']));
$dop=preg_replace("/\s{2,}/",' ',preg_replace('/[\r\n]{1,}/s',' ',$_POST['dop']));
$time=date('d.m.Y H:i:s');
$user=$_SERVER['REMOTE_ADDR'];

mysqli_query($db,"INSERT INTO `note`(`cont`,`dop`,`time`,`user`) VALUES ('$cont','$dop','$time','$user');");

$in=fopen('input.txt','a');
$out=fopen('output.txt','a');
fwrite($in,$cont.'
');
fwrite($out,$dop.'
');
fclose($in);
fclose($out);
?>