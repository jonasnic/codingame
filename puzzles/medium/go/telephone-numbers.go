package main

import (
  "fmt"
  "strings"
  "strconv"
)

type Node struct {
  digit int
  children []Node
}

func index(node *Node, digit int) int {
  for i, child := range node.children {
    if child.digit == digit {
      return i
    }
  }
  return -1
}

func addChild(node *Node, digit int) {
  var children []Node
  var child = Node{digit, children}
  node.children = append(node.children, child)
}

func main() {
  var nbPhones int
  fmt.Scan(&nbPhones)
  var nbNodes = 0
  var children []Node
  var root = Node{-1, children}

  for i := 0; i < nbPhones; i++ {
    var telephone string
    fmt.Scan(&telephone)
    var slice = strings.Split(telephone, "")

    var current = &root
    for _, value := range slice {
      var digit, _ = strconv.Atoi(value)
      var i = index(current, digit)
      if i == -1 {
        addChild(current, digit)
        nbNodes++
        i = index(current, digit)
      }
      current = &(current.children[i])
    }
  }
  
  fmt.Println(nbNodes)
}
