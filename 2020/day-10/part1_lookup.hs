-- https://mrmr.io/memoization-in-haskell

import Data.List          ( sort )

import System.Environment ( getArgs )
import System.IO          ( readFile )

type Cache = [(Int, Int)]

cachedCombs :: [Int] -> Int -> (Int, Cache)
cachedCombs xs x = combs xs x []

combs :: [Int] -> Int -> Cache -> (Int, Cache)
combs xs x ch
    | x == minimum xs = (1, ch)
    | x `notElem` xs = (0, ch)
    | otherwise = case lookup x ch of
        Just r -> (r, ch)
        Nothing -> let (r0, ch0) = combs xs (x - 1) ch
                       (r1, ch1) = combs xs (x - 2) ch0
                       (r2, ch2) = combs xs (x - 3) ch1
                       r = r0 + r1 + r2
            in (r, (x, r) : ch2)

main :: IO()
main = do
    args <- getArgs
    s <- readFile $ head args
    let adapters :: [Int] = sort $ read <$> lines s
    print $ fst $ cachedCombs (0:adapters) (maximum adapters)
