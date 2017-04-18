<?php
include('func.php');
$db=db();
header('location: ./');
$cont=text($_POST['cont']);
$dop=text($_POST['dop']);

if ($cont)
	{
	$t=True;
	$res=mysqli_query($db,"SELECT * FROM `note`");
	while($row=mysqli_fetch_array($res))
		if ($row['cont']==$cont)
			$t=False;
	if ($t)
		{
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
		}
	}
?>