<html>
<header>
  <link rel="stylesheet" href="styles.css">
  <link rel="shortcut icon" type ="image/jpg" href ="https://www.uark.edu/_resources/img/logo-on-red.png"/>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

	<title>Add Team</title>
</header>

<body>
<h5>
	<a class="goBack" href="http://www.csce.uark.edu/~ajtorres/project_python/index.html">
		<i class="fa fa-caret-square-o-left" style="font-size: 24px;"></i> &nbsp;Go Back</a>
</h5>
<h3>Add Team Page</h3>


<form action="addTeam.php" method="post">
	<p>
		<label for="teamName">Team Name: &nbsp;</label>
		<input id="teamName" type="text" name="teamName"><br>
	</p>
	<p>
		<label for="nickName">Nickname:</label>
		<input id="nickName" type="text" name="nickName"><br>
	</p>
	<p>
		<label for="wins">Wins:</label>
		<input id="wins" type="text" name="wins"><br>
	</p>
	<p>
		<label for="losses">Losses:</label>
		<input id="losses" type="text" name="losses"><br>
	</p>
	<p>
		<label for="rank">Rank:</label>
		<input id="rank" type="text" name="rank"><br>
	</p>
	<p>
		<br><br>
		<input type="submit" name="submit">
	</p>
</form>
<br><br>

</body>
</html>

<?php
if(isset($_POST['submit']))
{
	// add ' 's around names
	$teamName = escapeshellarg($_POST[teamName]);
	$nickName = escapeshellarg($_POST[nickName]);
	$wins = escapeshellarg($_POST[wins]);
	$losses = escapeshellarg($_POST[losses]);
	$rank = escapeshellarg($_POST[rank]);

	// build linux command
	$argument = "1";
	$command = "python3 main.py " . $argument . ' ' . $teamName . ' ' . $nickName . ' ' . $wins . ' ' . $losses . ' ' . $rank;

	// remove dangerous characters
	$escapedCommand = escapeshellcmd($command);

	// echo and run command
	echo "<p>command: $escapedCommand </p><br><br>";
	system($escapedCommand);
}
?>
