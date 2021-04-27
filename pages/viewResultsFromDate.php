<html>
<header>
  <link rel="stylesheet" href="styles.css">
  <link rel="shortcut icon" type ="image/jpg" href ="https://www.uark.edu/_resources/img/logo-on-red.png"/>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

	<title>View Results From Date</title>
</header>

<body>
<h5>
	<a class="goBack" href="http://www.csce.uark.edu/~ajtorres/project_python/index.html">
		<i class="fa fa-caret-square-o-left" style="font-size: 24px;"></i> &nbsp;Go Back</a>
</h5>

<h3>View Results From Date</h3>
	<form action="viewResultsFromDate.php" method="post">
		Please enter date using this format: YYYY-MM-DD <br>
		Date: <input type="text" name="date"><br>
		<input type="submit" name="submit">
	</form>
<br><br>
</body>
</html>


<?php
if (isset($_POST['submit']))
{
		// add ' 's around date
		$date = escapeshellarg($_POST[date]);

		// build linux command to be executed
		$argument = '6';
		$command = 'python3 main.py ' . $argument . ' ' . $date;

		//remove dangerous characters
		$command = escapeshellcmd($command);

		//echo then run the command
		echo "command: $command <br><br>";
		system($command);

}

?>
