<html>
<header>
  <link rel="stylesheet" href="styles.css">
  <link rel="shortcut icon" type ="image/jpg" href ="https://www.uark.edu/_resources/img/logo-on-red.png"/>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

	<title>Add Result</title>
</header>

<body>
<h5>
	<a class="goBack" href="http://www.csce.uark.edu/~ajtorres/project_python/index.html">
		<i class="fa fa-caret-square-o-left" style="font-size: 24px;"></i> &nbsp;Go Back</a>
</h5>

<h3>Add Result Page</h3>
<h4>Please enter the result information:</h4><br>
<form action="addResult.php" method="post">
	<p>
		<label for="gameID">Game ID:</label>
		<input id="gameID" type="text" name="gameID"><br>
	</p>
	<p>
		<label for="teamOneID">Team 1 ID:</label>
		<input id="teamOneID" type="text" name="teamOneID"><br>
	</p>
	<p>
		<label for="teamTwoID">Team 2 ID:</label>
		<input id="teamTwoID" type="text" name="teamTwoID"><br>
	</p>
	<p>
		<label for="teamOneScore">Team 1 Score:</label>
		<input id="teamOneScore" type="text" name="teamOneScore"><br>
	</p>
	<p>
		<label for="teamTwoScore">Team 2 Score:</label>
		<input id="teamTwoScore" type="text" name="teamTwoScore"><br>
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
	$gameID = escapeshellarg($_POST[gameID]);
	$teamOneID = escapeshellarg($_POST[teamOneID]);
	$teamTwoID = escapeshellarg($_POST[teamTwoID]);
	$teamOneScore = escapeshellarg($_POST[teamOneScore]);
	$teamTwoScore = escapeshellarg($_POST[teamTwoScore]);

	// build linux command
	$argument = "3";
	$command = "python3 main.py " . $argument . ' ' . $gameID . ' ' . $teamOneID . ' ' . $teamTwoID . ' ' . $teamOneScore . ' ' . $teamTwoScore;

	// remove dangerous characters
	$command = escapeshellcmd($command);

	// echo and run command
	echo "command: $command <br>";
	system($command);

}

?>
