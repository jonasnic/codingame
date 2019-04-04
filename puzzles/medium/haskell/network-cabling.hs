import System.IO
import Control.Monad
import Data.List

main :: IO ()
main = do
  hSetBuffering stdout NoBuffering -- DO NOT REMOVE
  
  input_line <- getLine
  let nbBuildings = read input_line :: Int
  
  list <- replicateM nbBuildings $ do
    input_line <- getLine
    let input = words input_line
    let x = read (input!!0) :: Int
    let y = read (input!!1) :: Int
    return (x, y)

  let coordinates = unzip list
  let xCoordinates = fst coordinates
  let yList = snd coordinates
  let yCoordinates = sort yList

  let minX = minimum xCoordinates
  let maxX = maximum xCoordinates
  let medianY = yCoordinates !! (nbBuildings `div` 2)
  let cableSize = foldl (\acc y -> acc + abs(medianY - y)) (maxX - minX) yCoordinates
  
  print cableSize
  return ()
