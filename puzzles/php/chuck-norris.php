<?php
// Convert the message into its binary representation.
function toBinary($msg) {
  $binaryMsg = "";
  for ($i = 0; $i < strlen($msg); ++$i) {
    $binary = decbin(ord($msg[$i]));
    $binaryMsg .= str_pad($binary, 7, "0", STR_PAD_LEFT);
  }
  return $binaryMsg;
}

// Convert the message into its unary representation.
function toUnary($msg) {
  $unaryMsg = "";
  $prevDigit = false; // false = 0, true = 1

  // first character
  if (strlen($msg) >= 1) {
    $char = $msg[0];
    if ($char == '0') {
      $unaryMsg .= "00 0"; // new sequence of zeros
    } else {
      $unaryMsg .= "0 0"; // new sequence of ones
      $prevDigit = true;
    }
  }

  for ($i = 1; $i < strlen($msg); ++$i) {
    $char = $msg[$i];
    if (($char == '0') && $prevDigit) {
      $unaryMsg .= " 00 0"; // Switch from 1 to 0
      $prevDigit = false;
    } else if (($char == '1') && !$prevDigit) {
      $unaryMsg .= " 0 0"; // Switch from 0 to 1
      $prevDigit = true;
    } else {
      $unaryMsg .= "0"; // Repeated 0 or 1
    }
  }
  return $unaryMsg;
}

$msg = stream_get_line(STDIN, 101, "\n");
$binaryMsg = toBinary($msg); 
echo(toUnary($binaryMsg) . "\n");
?>
