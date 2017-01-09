<?php
	$msg = "";
	if (isset($_POST['upload'])) {
		# code...
		//the path to store the upload image
		$target = "/var/www/html/images/".basename($_FILES['image']['name']);
		//Connect to the database
		//$db = mysql_connect("localhost","root","hero2009");
		echo $target;

		$con = mysql_connect('localhost', 'root', 'hero2009');
		echo "==========================";
		if (!$con) {
		    die('Not connected : ' . mysql_error());
		}else{
			echo "Connect mysql successfully!!!";
		}

		// make blog the current database
		$db_selected = mysql_select_db('photos', $con);
		if (!$db_selected) {
		    die ('blog not selected : ' . mysql_error());
		}else{
			echo "Connect mysql database photos successfully!!!";
		}
		
		//Get all the submitted data from the form
		$image = $_FILES['image']['name'];
		$text = $_POST['text'];

		echo $image;
		echo $text;		

		//$sql = "INSERT INTO images (image,text) VALUE('$image','$text')";
		$result = mysql_query("INSERT INTO images (image,text) VALUE('$image','$text')",$con);

		if(! $result )
		{
  			die('Could not get data: ' . mysql_error());
		}
		else
		{
			echo "Input into----------mysql database photos -----------------successfully!!!";
		}

		if (move_uploaded_file($_FILES['image']['tmp_name'], $target)) {
			$msg = "Image upload succeed!";
			# code...
		}else{
			$msg = "Image upload failed!";
		}
		echo $msg;
	}

?>



<!DOCTYPE html>
<html>
<head>
	<title>Image Upload</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<div id="content">
<?php
		$con = mysql_connect('localhost', 'root', 'hero2009');
		echo "==========================";
		if (!$con) {
		    die('Not connected : ' . mysql_error());
		}else{
			echo "Connect mysql successfully!!!";
		}

		// make blog the current database
		$db_selected = mysql_select_db('photos', $con);
		if (!$db_selected) {
		    die ('blog not selected : ' . mysql_error());
		}else{
			echo "Connect mysql database photos successfully!!!";
		}	

		//$sql = "INSERT INTO images (image,text) VALUE('$image','$text')";
		$result = mysql_query("SELECT * FROM images",$con);

		if(! $result )
		{
  			die('Could not get data: ' . mysql_error());
		}
		else
		{
			echo "Input into----------mysql database photos -----------------successfully!!!";
		}


		while($row = mysql_fetch_array($result))
		{
			echo "<div id = 'img_div'>";
			echo "<img src='images/".$row['image']."'>";
			echo "<p>".$row['text']."</p>";
			echo "</div>";
		}

?>




	<form method="post" action="index.php" enctype="multipart/form-data">
		<input type="hidden" name="size" value="1000000">
		<div>
			<input type="file" name="image">
		</div>
		<div>
			<textarea name="text" cols="40" rows="4" placeholder="say something...">
			</textarea>
		</div>
		<div>
			<input type="submit" name="upload" value="Upload Image">
		</div>
	</form>
</div>
</body>
</html>
