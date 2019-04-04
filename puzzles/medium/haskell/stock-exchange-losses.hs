import System.IO
import Control.Monad

main :: IO ()
main = do
  hSetBuffering stdout NoBuffering -- DO NOT REMOVE
  
  input_line <- getLine
  let nbValues = read input_line :: Int
  input_line <- getLine
  let values = map (read :: String -> Int) (words input_line)
  let loss = computeMaxLoss values (-1) 0
  
  print (-loss)
  return ()

computeMaxLoss :: [Int] -> Int -> Int -> Int
computeMaxLoss [] _ maxLoss = maxLoss
computeMaxLoss (y:ys) maxValue maxLoss
  | y > maxValue = computeMaxLoss ys y maxLoss
  | otherwise = computeMaxLoss ys maxValue (max maxLoss (maxValue - y))
