package main

import (
  "fmt"
  "os"
  "bufio"
  "strings"
  "strconv"
)

func printNextRoom(roomType int, x int, y int, entrance string) {
  if roomType == 2 || roomType == 6 {
    if entrance == "LEFT" {
      x++
    } else {
      x--
    }
  } else if roomType == 4 {
    if entrance == "TOP" {
      x--
    } else {
      y++
    }
  } else if (roomType == 5) {
    if entrance == "TOP" {
      x++
    } else {
      y++
    }
  } else if roomType == 10 {
    x--
  } else if roomType == 11 {
    x++
  } else {
    y++
  }

  fmt.Printf("%v %v\n", x, y)
}

func main() {
  var rooms []int
  scanner := bufio.NewScanner(os.Stdin)
  scanner.Buffer(make([]byte, 1000000), 1000000)

  var nbColumns, nbRows int
  scanner.Scan()
  fmt.Sscan(scanner.Text(), &nbColumns, &nbRows)
  
  for i := 0; i < nbRows; i++ {
    scanner.Scan()
    line := strings.Split(scanner.Text(), " ")
    for _, value := range line {
      var room, _ = strconv.Atoi(value)
      rooms = append(rooms, room)
    }
  }

  var ex int
  scanner.Scan()
  fmt.Sscan(scanner.Text(), &ex)
  
  // game loop
  for {
    var x, y int
    var entrance string
    scanner.Scan()
    fmt.Sscan(scanner.Text(), &x, &y, &entrance)
    printNextRoom(rooms[y * nbColumns + x], x, y, entrance)
    // fmt.Fprintln(os.Stderr, "Debug messages...")
  }
}
