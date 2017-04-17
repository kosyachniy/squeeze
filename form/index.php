<?php
include('func.php');
$db=db();
act('');
?>
<style>
	html, body {margin: 0; padding: 0;}
	p, textarea, input {font-family: Arial; font-size: 2.7vh;}
	p {margin: 2.5vh 0 0 0; width: 100vw; text-align: center;}
	textarea, input {width: 80vw; margin: 2.5vh 0 0 10vw; padding: 10px; border: 1px solid #000; border-radius: 15px;}
	textarea {height: 33vh;}
	input {background-color: #fff; color: #000; height: 7vh;}
	input:hover {background-color: #000; color: #fff; cursor: pointer;}
</style>
<!Doctype html>
<html>
	<head>
	    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=yes">
	    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title>Lacuna</title>
    	<link rel ="shortcut icon" type="images/png" href="logo.png">
    	<meta name="apple-mobile-web-app-capable" content="yes" />
	</head>
	<body style="zoom: 1;">
		<form action="new.php" method="post">
			<p>Начальный текст</p>
			<textarea name="cont"></textarea>
			<p>Сокращённый текст</p>
			<textarea name="dop"></textarea>
			<input type="submit" value="Добавить">
		</form>
	</body>
</html>