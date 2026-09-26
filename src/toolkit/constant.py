from datetime import datetime

OPERATORS = {'*', '/', '//', '%', '+', '-'}
def check_type(a: int, b: int) -> bool:
    return type(a) == type(b)
def reduction(value: str) -> str:
    while value.count('--'): value = value.replace('--', '+')
    while value.count('++'): value = value.replace('++', '+')
    return value

length_units = ['mm', 'cm', 'm', 'km']
mass_units = ['g', 'kg']
temp_units = ['c', 'k', 'f']
length_to_m = {
    'mm': 0.001,
    'cm': 0.01,
    'm': 1.0,
    'km': 1000
}
mass_to_g = {
    'g': 0.001,
    'kg': 1.0,
}

YEAR, MONTH, DAY, HOUR, MINUTE = datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour, datetime.now().minute
