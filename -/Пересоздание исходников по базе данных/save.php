<?php
//set_time_limit(100);
include('func.php');
$db=db();
$in=fopen('input.txt','w');
$out=fopen('output.txt','w');
$res=mysqli_query($db,"SELECT * FROM `note`");
while($i=mysqli_fetch_array($res))
	{
	fwrite($in,$i['cont'].'
');
	fwrite($out,$i['dop'].'
');
//	sleep(1);
	}
fclose($in);
fclose($out);
?>