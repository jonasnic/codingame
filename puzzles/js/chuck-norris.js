"use strict";

// Convert the string into its binary representation.
function toBinary(msg) {
  let binaryMsg = "";
  for (let i = 0; i < msg.length; ++i) {
    let asciiBin = msg[i].charCodeAt(0).toString(2)
    while (asciiBin.length < 7) {
      asciiBin = `0${asciiBin}`;
    }
    binaryMsg += asciiBin;
  }
  return binaryMsg;
}

// Convert the string into its unary representation.
function toUnary(msg) {
  let unaryMsg = "";
  let prevDigit = false; // false = 0, true = 1
  let character;

  // first character
  if (msg.length >= 1) {
    character = msg[0];
    if (character === '0') {
      unaryMsg += "00 0"; // new sequence of zeros
    } else {
      unaryMsg += "0 0"; // new sequence of ones
      prevDigit = true;
    }
  }

  for (let i = 1; i < msg.length; ++i) {
    character = msg[i];
    if ((character === '0') && prevDigit) { // Switch from 1 to 0
      unaryMsg += " 00 0";
      prevDigit = false;
    } else if ((character == '1') && !prevDigit) { // Switch from 0 to 1
      unaryMsg += " 0 0";
      prevDigit = true;
    } else { // Repeated 0 or 1
      unaryMsg += "0";
    }
  }
  return unaryMsg;
}

let msg = readline();
let binary = toBinary(msg);
print(toUnary(binary));
