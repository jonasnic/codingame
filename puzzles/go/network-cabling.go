package main

import (
  "fmt"
  "math"
  "sort"
)

func main() {
  var minX = 1073741824.0
  var maxX = 0.0
  var cableSize = 0.0
  var coordinates []float64

  var nbBuildings int
  fmt.Scan(&nbBuildings)
    
  for i := 0; i < nbBuildings; i++ {
    var x, y float64
    fmt.Scan(&x, &y)
    coordinates = append(coordinates, y)
    if x < minX {
      minX = x
    }
    if x > maxX {
      maxX = x
    }
  }

  sort.Float64s(coordinates)
  cableSize = maxX - minX
  
  // To minimize the total vertical length of the cables,
  // the y value of the main cable must be the median of all the y values.
  var median = coordinates[nbBuildings / 2]
  for i := 0; i < nbBuildings; i++ {
    cableSize += math.Abs(median - coordinates[i])
  }

  fmt.Println(int(cableSize))
}
