<html>
<header>
  <link rel="stylesheet" href="styles.css">
  <link rel="shortcut icon" type ="image/jpg" href ="https://www.uark.edu/_resources/img/logo-on-red.png"/>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

	<title>View All Teams</title>
</header>

<body>
<h5>
	<a class="goBack" href="http://www.csce.uark.edu/~ajtorres/project_python/index.html">
		<i class="fa fa-caret-square-o-left" style="font-size: 24px;"></i> &nbsp; Go Back</a>
</h5>
<h3>View All Teams Page</h3>
</body>
</html>

<?php
	$argument = '4';
	$command = 'python3 main.py ' . $argument;

	// echo then run the command
	echo "command: $command <br><br>";
	system($command);
?>
