import System.IO
import Control.Monad
import Data.Maybe

main :: IO ()
main = do
  hSetBuffering stdout NoBuffering -- DO NOT REMOVE
  
  input_line <- getLine
  let input = words input_line
  let exitFloor = read (input!!3) :: Int -- floor on which the exit is found
  let exitPos = read (input!!4) :: Int -- position of the exit on its floor
  let nbElevators = read (input!!7) :: Int -- number of elevators
  
  elevators <- replicateM nbElevators $ do
    input_line <- getLine
    let input = words input_line
    let elevatorFloor = read (input!!0) :: Int -- floor on which this elevator is found
    let elevatorPos = read (input!!1) :: Int -- position of the elevator on its floor
    return (elevatorFloor, elevatorPos)
  
  -- game loop
  forever $ do
    input_line <- getLine
    let input = words input_line
    let cloneFloor = read (input !! 0) :: Int -- floor of the leading clone
    let clonePos = read (input !! 1) :: Int -- position of the leading clone on its floor
    let direction = input !! 2 -- direction of the leading clone: LEFT or RIGHT
    
    if cloneFloor == -1 then
      putStrLn "WAIT"
    else if cloneFloor == exitFloor then
      if direction == "LEFT" && clonePos < exitPos then
        putStrLn "BLOCK"
      else if direction == "RIGHT" && clonePos > exitPos then
        putStrLn "BLOCK"
      else
        putStrLn "WAIT"
    else do
      let elevatorPos = fromJust (lookup cloneFloor elevators)
      if direction == "LEFT" && clonePos < elevatorPos then
        putStrLn "BLOCK"
      else if direction == "RIGHT" && clonePos > elevatorPos then
        putStrLn "BLOCK"
      else
        putStrLn "WAIT"
