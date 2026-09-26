from .tokenization import tokenization
from .validation import validation
from .estimation import estimation



def calculate(expression: list[str]) -> float:
    tokens = tokenization(expression)
    validation(tokens)
    return estimation(tokens)

