package main

import (
  "fmt"
  "os"
  "bufio"
  "strings"
  "strconv"
)

func main() {
  var maxValue int64 = -1
  var maxLoss int64 = 0

  scanner := bufio.NewScanner(os.Stdin)
  scanner.Buffer(make([]byte, 1000000), 1000000)

  var nbValues int
  scanner.Scan()
  fmt.Sscan(scanner.Text(), &nbValues)
  
  scanner.Scan()
  inputs := strings.Split(scanner.Text(), " ")
  for i := 0; i < nbValues; i++ {
    value, _ := strconv.ParseInt(inputs[i], 10, 32)
    if value > maxValue {
      maxValue = value
    } else {
      var loss = maxValue - value
      if (loss > maxLoss) {
        maxLoss = loss
      }
    }
  }
  
  // fmt.Fprintln(os.Stderr, "Debug messages...")
  fmt.Println(-maxLoss)// Write answer to stdout
}
