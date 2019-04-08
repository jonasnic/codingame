import System.IO
import Control.Monad

main :: IO ()
main = do
  hSetBuffering stdout NoBuffering -- DO NOT REMOVE
  
  input_line <- getLine
  let surfacen = read input_line :: Int
  
  replicateM surfacen $ do
    input_line <- getLine
    return ()
  
  -- game loop
  forever $ do
    input_line <- getLine
    let input = words input_line
    let x = read (input!!0) :: Int
    let y = read (input!!1) :: Int
    let hspeed = read (input!!2) :: Int
    let vspeed = read (input!!3) :: Int -- the vertical speed (in m/s), can be negative.
    let fuel = read (input!!4) :: Int
    let angle = read (input!!5) :: Int
    let power = read (input!!6) :: Int -- the thrust power (0 to 4).
    
    -- hPutStrLn stderr "Debug messages..."
    
    -- 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
    
    if vspeed <= -40 then
      putStrLn(show angle ++ " 4")
    else
      putStrLn(show angle ++ " 0")
