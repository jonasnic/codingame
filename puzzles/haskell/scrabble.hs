import System.IO
import Control.Monad
import qualified Data.Map as Map
import qualified Data.List as List
import qualified Data.Maybe as Maybe

main :: IO ()
main = do
  hSetBuffering stdout NoBuffering -- DO NOT REMOVE
  
  let table = Map.fromList [('e', 1), ('a', 1), ('i', 1),
                             ('o', 1), ('n', 1), ('r', 1),
                             ('t', 1), ('l', 1), ('s', 1),
                             ('u', 1), ('d', 2), ('g', 2),
                             ('b', 3), ('c', 3), ('m', 3),
                             ('p', 3), ('f', 4), ('h', 4),
                             ('v', 4), ('w', 4), ('y', 4),
                             ('k', 5), ('j', 8), ('x', 8),
                             ('q', 10), ('z', 10)] :: Map.Map Char Int

  input_line <- getLine
  let nbWords = read input_line :: Int
  words <- replicateM nbWords $ do
    word <- getLine
    return word
  letters <- getLine

  let scores = map (wordScore letters table) words
  let maxScore = maximum scores
  let indexMax = Maybe.fromJust $ List.elemIndex maxScore scores
  let bestWord = words !! indexMax

  putStrLn bestWord
  return ()

wordScore :: String -> Map.Map Char Int -> String -> Int
wordScore letters table word =
  let diff = word List.\\ letters in
  if (length diff) == 0 then
    foldl (\acc letter -> acc + (letterScore letter table)) 0 word
  else
    0

letterScore :: Char -> Map.Map Char Int -> Int
letterScore letter table = case (Map.lookup letter table) of
  Just score -> score
  Nothing -> 0
