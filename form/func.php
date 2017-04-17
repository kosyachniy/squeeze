<?php
header('Content-type: text/html; charset=utf-8');
function db()
	{
	//$db=mysqli_connect('localhost','root','a18988189a','lacuna');
	$db=mysqli_connect('mysql.hostinger.ru','u696001181_k','asdrqwerty09','u696001181_k');
	if (mysqli_connect_errno()) print 'Ошибка #1: '.mysqli_connect_errno();
	mysqli_query($db,'SET names "utf8"');
	return $db;
	}
?>