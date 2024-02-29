import Control.Monad

import Data.Default

import Text.Read

shead :: forall a. Default a => [a] -> a
shead []     = def :: a
shead (x:xs) = x

stail :: [a] -> [a]
stail []     = []
stail (x:xs) = xs

mshow :: Maybe Int -> String
mshow (Just x) = show x
mshow Nothing  = ""

summ :: [Maybe Int] -> Maybe Int
summ = foldl (liftM2 (+)) (Just 0)

normalize :: String -> String
normalize [] = []
normalize (x:xs) = unBr x ++ normalize xs
    where
        unBr '(' = "( "
        unBr ')' = " )"
        unBr c   = [c]

checkNum :: String -> Maybe Int
checkNum s = readMaybe s :: Maybe Int

oper :: String -> Maybe Int -> Maybe Int -> Maybe Int
oper "" x _ = x
oper _ _ Nothing = Nothing
oper _ Nothing _ = Nothing
oper op (Just x) (Just y)
    | op == "+" = Just (x + y)
    | op == "*" = Just (x * y)


solveEq :: [String] -> String -> [String] -> [Maybe Int] -> Int -> Maybe Int
solveEq [] _ _ xs 0 = shead xs
solveEq [] _ _ xs l = Nothing
solveEq ("(":xs) op ops ints lev = solveEq xs "" (op:ops) ints (lev + 1)
solveEq (")":xs) _ ops ints lev =
    let o = shead ops
        i = mshow . shead $ ints
    in solveEq (i:xs) o (stail ops) (stail ints) (lev - 1)
solveEq ("+":xs) _ ops ints lev = solveEq xs "+" ops ints lev
solveEq ("*":xs) _ ops ints lev = solveEq xs "*" ops ints lev
solveEq (x:xs) o ops ints lev
    | o == "" =
        let i = readMaybe x :: Maybe Int
        in solveEq xs o ops (i:ints) lev
    | otherwise =
        let i = readMaybe x :: Maybe Int
            ii = shead ints
            iints = stail ints
            ni = oper o i ii
        in solveEq xs "" ops (ni:iints) lev

solverEq :: [String] -> Maybe Int
solverEq xs = solveEq xs "" [] [] 0

main :: IO()
main = interact $ show . summ . (map solverEq) . (map words) . (map normalize) . lines
