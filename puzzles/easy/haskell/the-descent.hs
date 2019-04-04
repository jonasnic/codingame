import System.IO
import Control.Monad
import Data.List
import Data.Maybe

main :: IO ()
main = do
  hSetBuffering stdout NoBuffering -- DO NOT REMOVE
    
  -- game loop
  forever $ do
    heights <- replicateM 8 $ do
      input_line <- getLine
      let height = read input_line :: Int -- represents the height of one mountain.
      return height
    
    let maxHeight = maximum heights
    let indexMax = fromJust $ elemIndex maxHeight heights
    
    -- The index of the mountain to fire on.
    putStrLn (show indexMax)
