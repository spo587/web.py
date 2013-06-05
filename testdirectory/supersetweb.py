$def with (printboard, printthesupersets, numsupersetsonboard)

<html>
<head>
	<link rel="stylesheet" href='/static/helloworld.css' />
</head>
<body>
	

	
$for cardnumber in printboard[0:3]:
	<img src=$cardnumber>

<br />

$for cardnumber in printboard[3:6]:
	<img src=$cardnumber>

<br />

$for cardnumber in printboard[6:9]:
	<img src=$cardnumber>

<br/>

$if len(printboard) > 9:
    $for cardnumber in printboard[9:12]:
        <img src=$cardnumber>
    
	
<br />


<br><br/><br><br/><br><br/><br><br/><br><br/><br><br/><br><br/><br><br/><br><br/><br><br/>

$numsupersetsonboard

<br><br/><br><br/><br><br/><br><br/><br><br/><br><br/><br><br/><br><br/><br><br/><br><br/>

$if len(printthesupersets) == 0:
	deadboard!!!
	
$if len(printthesupersets) > 0:
	$for number in printthesupersets[0:4]:
		<img src=$number>
<br/>

$if len(printthesupersets) > 4:
	$for number in printthesupersets[4:8]:
		<img src=$number>
		
<br/>

$if len(printthesupersets) > 8:
	$for number in printthesupersets[8:12]:
		<img src=$number>
		
<br/>

$if len(printthesupersets) > 12:
	$for number in printthesupersets[12:16]:
		<img src=$number>
		
<br/>

$if len(printthesupersets) > 16:
	$for number in printthesupersets[16:20]:
		<img src=$number>
		
<br/>