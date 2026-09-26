from decimal import Decimal
from .errors import * 
from .constant import OPERATORS, check_type


def validation(tokens: list[str]) -> None:
    if not tokens:
        missed_number()
        
    if check_type(tokens[0], ''):
        if tokens[0] not in '+-':
            wrong_start_expression(tokens[0])
            
        tokens = tokens[1:]
    if not tokens:
        missed_number()
        
    if check_type(tokens[-1], ''):
        missed_number()
    
    for i in range(len(tokens)-1):
        if check_type(tokens[i], '') and check_type(tokens[i+1], ''):
            if tokens[i] not in '+-':
                if tokens[i+1] not in '+-':
                    double_operands()
                    
                if i+2 >= len(tokens) or check_type(tokens[i+2], ''):
                    missed_number()
            else:
                if i+2 >= len(tokens) or check_type(tokens[i+2], ''):
                    missed_number()

def check_unary(tokens: list) -> list:
    result = []
    i = 0
    while i < len(tokens):
        mark = check_type(tokens[i], '') and tokens[i] in '+-'
        after_op = (i and check_type(tokens[i-1], '') and tokens[i-1] in OPERATORS)
        after_mark = (i and check_type(tokens[i-1], '') and tokens[i-1] in '+-')
        next_number = (i < len(tokens)-1 and check_type(tokens[i+1], Decimal('1')))

        if mark and (i==0 or after_op or after_mark) and next_number:
            if tokens[i] == '+': result.append(tokens[i+1])
            else: result.append(Decimal('-1')(tokens[i+1]))
            i += 2
        else:
            result.append(tokens[i])
            i += 1
    return result