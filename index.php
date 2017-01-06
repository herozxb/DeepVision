<?php
	$msg = "";
	if (isset($_POST['upload'])) {
		# code...
		//the path to store the upload image
		$target = "images/".basename($_FILES['iamge']['name']);
		//Connect to the database
		$db = mysql_connect("localhost","root","","photos");

		//Get all the submitted data from the form
		$image = $_FILES['image']['name'];
		$text = $_POST['text'];

		$sql = "INSERT INTO images (image,text) VALUE('$image','$text')";
		mysql_query($db,$sql);

		if (move_uploaded_file($_FILES['tmp_name']['name'], $target)) {
			$msg = "Image upload succeed!";
			# code...
		}else{
			$msg = "Image upload failed!";
		}
	}

?>



<!DOCTYPE html>
<html>
<head>
	<title>Image Upload</title>
</head>
<body>
<div id="content">
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