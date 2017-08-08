<?php
$blacklists = Array('$', 'IFS', 'cat', 'flag', '65', '41', ' ', '|');

function contains($str, array $arr)
{
    foreach($arr as $a) {
        if (stripos($str,$a) !== false) return true;
    }
    return false;
}

if($admin){
	$f = $_GET['f'];
	if(strlen($f) > 115)die("masa format date panjang gitu, hmmm mencurigakan...");
        $fmt = base64_decode($_GET['f']);
        if(contains($fmt, $blacklists)) die("no attacker allowed!!!");
	eval('echo date("'.$fmt.'");');
	die();
}

die("only admin can see my day!");
?>
