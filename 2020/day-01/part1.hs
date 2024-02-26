pairs :: [Int] -> [(Int, Int)]
pairs ds = [(x, y) | x <- ds, y <- ds]

triples :: [Int] -> [(Int, Int, Int)]
triples ds = [(x, y, z) | x <- ds, y <- ds, z <- ds]

findPair :: [Int] -> Int -> (Int, Int)
findPair ds tgt =
    let ps = pairs ds
    in head $ filter (\(x, y) -> x + y == tgt) ps

findTriple :: [Int] -> Int -> (Int, Int, Int)
findTriple ds tgt =
    let ps = triples ds
    in head $ filter (\(x, y, z) -> x + y + z == tgt) ps

solvePair :: [Int] -> Int
solvePair xs =
    let (x, y) = findPair xs 2020
    in x * y

solveTriple :: [Int] -> Int
solveTriple xs =
    let (x, y, z) = findTriple xs 2020
    in x * y * z

main :: IO()
main =
    let solve = sequence [solvePair, solveTriple]
    in interact $ unlines . (map show) . solve . map read . lines
