<?php
header('Content-type: text/html; charset=utf-8');

function db()
	{
	$db=mysqli_connect('mysql.hostinger.ru','u696001181_k','asdrqwerty09','u696001181_k');
	if (mysqli_connect_errno()) print 'Ошибка #1: '.mysqli_connect_errno();
	mysqli_query($db,'SET names "utf8"');
	return $db;
	}

function act($cont)
	{
	$user=$_SERVER['REMOTE_ADDR'];
	$time=date('d.m.Y H:i:s');
	mysqli_query($db,"INSERT INTO `act`(`cont`,`user`,`time`) VALUES ('$cont','$user','$time');");
	}

function text($cont)
	{
	return preg_replace("/\s{2,}/",' ',preg_replace('/[\r\n]{1,}/s',' ',$cont))
	}
?>