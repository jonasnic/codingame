import System.IO
import Control.Monad

main :: IO ()
main = do
  hSetBuffering stdout NoBuffering -- DO NOT REMOVE
  
  input_line <- getLine
  let input = words input_line
  let lightX = read (input!!0) :: Int
  let lightY = read (input!!1) :: Int
  let thorX = read (input!!2) :: Int
  let thorY = read (input!!3) :: Int
  
  playTurn lightX lightY thorX thorY

playTurn lightX lightY thorX thorY =
  if thorY > lightY && thorX > lightX then do
    putStrLn "NW"
    playTurn lightX lightY (thorX - 1) (thorY - 1)
  else if thorY > lightY && thorX < lightX then do
    putStrLn "NE"
    playTurn lightX lightY (thorX + 1) (thorY - 1)
  else if thorY < lightY && thorX > lightX then do
    putStrLn "SW"
    playTurn lightX lightY (thorX - 1) (thorY + 1)
  else if thorY < lightY && thorX < lightX then do
    putStrLn "SE"
    playTurn lightX lightY (thorX + 1) (thorY + 1)
  else if  thorX > lightX then do
    putStrLn "W"
    playTurn lightX lightY (thorX - 1) thorY
  else if  thorX < lightX then do
    putStrLn "E"
    playTurn lightX lightY (thorX + 1) thorY
  else if  thorY > lightY then do
    putStrLn "N"
    playTurn lightX lightY thorX (thorY - 1)
  else if  thorY < lightY then do
    putStrLn "S"
    playTurn lightX lightY thorX (thorY + 1)
  else do
    putStrLn ""
    playTurn lightX lightY thorX thorY
