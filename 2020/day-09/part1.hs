import Control.Monad      ( liftM2 )

import Safe               ( atMay )

import System.Environment ( getArgs )
import System.IO          ( readFile )

combs :: Int -> [a] -> [[a]]
combs 0 _      = [[]]
combs _ []     = []
combs n (x:xs) = map (x :) (combs (n - 1) xs) ++ combs n xs

slice :: Int -> Int -> [Int] -> [Int]
slice i j
    | i < j = drop (i - 1) . take j
    | otherwise = drop (j - 1) . take i

wrongNum :: [Int] -> [Int] -> Maybe Int
wrongNum _ [] = Nothing
wrongNum hd@(_:hs) (t:ts) = let
      chck = filter ((== t) . sum) $ combs 2 hd
      in case chck of
          []        -> Just t
          _NonEmpty -> wrongNum (hs ++ [t]) ts

(!+!) = liftM2 (+)
(!-!) = liftM2 (-)
(!!!) = atMay

solve1 :: Int -> [Int] -> Maybe Int
solve1 n xs = wrongNum (take n xs) (drop n xs)

seqNum :: Int -> Int -> Maybe Int -> Maybe Int -> [Int] -> Maybe Int
seqNum _ _ _ Nothing _ = Nothing
seqNum _ _ Nothing _ _ = Nothing
seqNum i j acc num xs
    | i > len || j > len = Nothing
    | otherwise = case liftM2 compare acc num of
        Just EQ -> Just (minimum sl + maximum sl)
        Just LT -> seqNum i (j + 1) (acc !+! (xs !!! (j + 1))) num xs
        Just GT -> seqNum (i + 1) j (acc !-! (xs !!! i)) num xs
    where
        len = length xs - 1
        sl = slice i j xs

main :: IO()
main = do
    args <- getArgs
    s <- readFile $ head args
    let nums = read <$> lines s
    let ans1 = solve1 25 nums
    let ans2 = seqNum 0 0 (Just $ head nums) ans1 nums
    print [ans1, ans2]
