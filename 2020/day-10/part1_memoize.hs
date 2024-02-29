-- https://stackoverflow.com/questions/3208258/memoization-in-haskell

import Data.List          ( sort )

import System.Environment ( getArgs )
import System.IO          ( readFile )

memoize :: (([Int] -> Int -> Integer) -> [Int] -> Int -> Integer) -> [Int] -> Int -> Integer
memoize f xs = memoizedF xs
    where
        memoizedF xs = (memory !!)
        memory = map (f memoizedF xs) [0..]

combs :: ([Int] -> Int -> Integer) -> [Int] -> Int -> Integer
combs f xs x
    | x `notElem` xs = 0
    | x == maximum xs = 1
    | otherwise = sum [f xs nx | nx <- [x + 1 .. x + 3], nx `elem` xs]

memoizedCombs :: [Int] -> Int -> Integer
memoizedCombs = memoize combs

main :: IO()
main = do
    args <- getArgs
    s <- readFile $ head args
    let adapters :: [Int] = sort $ read <$> lines s
    print $ memoizedCombs (0:adapters) 0
