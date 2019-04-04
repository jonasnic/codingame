package main

import (
  "fmt"
  "os"
  "bufio"
)

func toBinary(text string) string {
  var binaryText = ""
  for _, r := range text {
    binaryText += fmt.Sprintf("%.7b", r)
  }
  return binaryText
}

func toUnary(text string) string {
  var unaryText = ""
  var prevDigit = false // false = 0, true = 1
  // handle first character
  if len(text) >= 1 {
    var c = text[0]
    if c == '0' {
      unaryText += "00 0"
    } else {
      unaryText += "0 0"
      prevDigit = true
    }
  }

  for i := 1; i < len(text); i++ {
    var c = text[i]
    if c == '0' && prevDigit {
      unaryText += " 00 0" // switch from 1 to 0
      prevDigit = false
    } else if c == '1' && !prevDigit {
      unaryText += " 0 0" // switch from 0 to 1
      prevDigit = true
    } else {
      unaryText += "0"
    }
  }

  return unaryText
}

func main() {
  scanner := bufio.NewScanner(os.Stdin)
  scanner.Buffer(make([]byte, 1000000), 1000000)

  scanner.Scan()
  text := scanner.Text()
  var binaryText = toBinary(text)
  var unaryText = toUnary(binaryText)
  
  fmt.Println(unaryText)// Write answer to stdout
}
