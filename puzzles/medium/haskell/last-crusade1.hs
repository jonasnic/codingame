import System.IO
import Control.Monad
import Text.Printf

main :: IO ()
main = do
  hSetBuffering stdout NoBuffering -- DO NOT REMOVE
  
  input_line <- getLine
  let input = words input_line
  let width = read (input!!0) :: Int
  let height = read (input!!1) :: Int
  
  rooms <- replicateM height $ do
    line <- getLine
    let row = map (read::String->Int) (words line)
    return row
  input_line <- getLine
  let ex = read input_line :: Int
  
  -- game loop
  forever $ do
    input_line <- getLine
    let input = words input_line
    let x = read (input !! 0) :: Int
    let y = read (input !! 1) :: Int
    let entrance = input !! 2
    
    printNextRoom ((rooms !! y) !! x) x y entrance

printNextRoom :: Int -> Int -> Int -> String -> IO ()
printNextRoom roomType x y entrance = do
  if roomType == 2 || roomType == 6 then
    if entrance == "LEFT" then
      printf "%d %d\n" (x + 1) y
    else
      printf "%d %d\n" (x - 1) y
  else if roomType == 4 then
    if entrance == "TOP" then
      printf "%d %d\n" (x - 1) y
    else
      printf "%d %d\n" x (y + 1)
  else if roomType == 5 then
    if entrance == "TOP" then
      printf "%d %d\n" (x + 1) y
    else
      printf "%d %d\n" x (y + 1)
  else if roomType == 10 then
    printf "%d %d\n" (x - 1) y
  else if roomType == 11 then
    printf "%d %d\n" (x + 1) y
  else
    printf "%d %d\n" x (y + 1)
