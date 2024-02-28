import Data.Char (isDigit, isSpace)
import Text.ParserCombinators.ReadP

data Expr =
    OpExpr Char Expr Expr | NumExpr Int
    deriving Show

pExpr :: ReadP Expr
pExpr = pTerminal `chainl1` pOperator
    where
        pOpSymbol op = skipSpaces *> char op <* skipSpaces
        pOperator = (OpExpr <$> pOpSymbol '+') +++ (OpExpr <$> pOpSymbol '*')
        pNumber = NumExpr . read <$> munch1 isDigit
        pBrackets = between (char '(') (char ')') pExpr
        pTerminal = pNumber +++ pBrackets

pExprP :: ReadP Expr
pExprP = pAddExpr `chainl1` (OpExpr <$> pOpSymbol '*')
    where
        pOpSymbol op = skipSpaces *> char op <* skipSpaces
        pNumber = NumExpr . read <$> munch1 isDigit
        pBrackets = between (char '(') (char ')') pExprP
        pTerminal = pNumber +++ pBrackets
        pAddExpr = pTerminal `chainl1` (OpExpr <$> pOpSymbol '+')


evalExpr :: Expr -> Int
evalExpr (OpExpr '+' x y) = evalExpr x + evalExpr y
evalExpr (OpExpr '*' x y) = evalExpr x * evalExpr y
evalExpr (NumExpr x) = x

solve1 :: [String] -> Int
solve1 = sum . map (evalExpr . fst . last . readP_to_S pExpr)

solve2 :: [String] -> Int
solve2 = sum . map (evalExpr . fst . last . readP_to_S pExprP)

solve = sequence [solve1, solve2]

main :: IO()
main = interact $ unlines . map show . solve . lines
