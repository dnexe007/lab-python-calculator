from src.tokenization import tokenize
from src.conversion_to_rpn import to_rpn
from src.calculation import calculate

def run_calculator(expression: str) -> float:
    return calculate(to_rpn(tokenize(expression)))
