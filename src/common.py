from re import match

# проверка, является ли токен корректным числом
def is_number(num: str) -> bool:
    pattern = r'^([0-9]*\.?[0-9]+)$'
    return match(pattern, num) is not None

# операторы и приоритеты
OPERATORS: list[str] = ["+", "-", "*", "/", "^", "%", "#"]
UNARY_OPERATORS: list[str] = ["u-", "u+"]
PRIORITIES: dict = {'+':1, '-':1, '*':2, '/':2, '#': 2, '%':2, '^':3, 'u+':4, 'u-':4}
