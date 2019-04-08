import System.IO
import Control.Monad

main :: IO ()
main = do
  hSetBuffering stdout NoBuffering -- DO NOT REMOVE
  
  input_line <- getLine
  -- the number of temperatures to analyse
  let n = read input_line :: Int
  input_line <- getLine
  let temperatures = map (read :: String -> Int) (words input_line)
  
  if n == 0 then
    print 0
  else
    print $ computeMin temperatures

  return ()

computeMin :: [Int] -> Int
computeMin (t:[]) = t
computeMin (t:ts) = t `min2` computeMin ts

min2 :: Int -> Int -> Int
min2 x y
  | abs(x) < abs(y) = x
  | abs(x) > abs(y) = y
  | abs(x) == abs(y) && x > y = x
  | otherwise = y
