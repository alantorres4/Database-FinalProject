<html>
<header>
	<link rel="stylesheet" href="styles.css">
  <link rel="shortcut icon" type ="image/jpg" href ="https://www.uark.edu/_resources/img/logo-on-red.png"/>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

	<title>Add Game</title>
</header>

<body>
<h5>
	<a class="goBack" href="http://www.csce.uark.edu/~ajtorres/project_python/index.html">
		<i class="fa fa-caret-square-o-left" style="font-size: 24px;"></i> &nbsp;Go Back</a>
</h5>

<h3>Add Game Page</h3>
<h4>Please enter the game information: </h4>

<form action="addGame.php" method="post">
	<p>
		<label for="teamOneID">Team 1 ID: &nbsp; </label>
		<input id="teamOneID" type="text" name="teamOneID"><br>
	</p>
	<p>
		<label for="teamTwoID">Team 2 ID:</label>
		<input id="teamTwoID" type="text" name="teamTwoID"><br>
	</p>
	<p>
		<label for="location">Location:</label>
		<input id="location" type="text" name="location"><br>
	</p>
	<p>
		<label for="date">Date:</label>
		<input type="text" name="date"><br>
	</p>
	<p>
		<input type="submit" name="submit">
	</p>
</form>
<br><br>

</body>
</html>

<?php
if(isset($_POST['submit']))
{
	$teamOneID = escapeshellarg($_POST[teamOneID]);
	$teamTwoID = escapeshellarg($_POST[teamTwoID]);
	$location = escapeshellarg($_POST[location]);
	$date = escapeshellarg($_POST[date]);

	// build linux command
	$argument = "2";
	$command = "python3 main.py " . $argument . ' ' . $teamOneID . ' ' . $teamTwoID . ' ' . $location . ' ' . $date;

	// remove dangerous characters
	$command = escapeshellcmd($command);

	// echo then run the command
	echo "command: $command <br><br>";
	system($command);
}

?>
