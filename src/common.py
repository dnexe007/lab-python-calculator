from re import match


def is_number(num: str) -> bool:
    """
    Проверка регулярным выражением, является ли строка корректным числом
    :param num: Строка для проверки
    :return: Является ли строка числом
    """
    pattern = r'^([0-9]*\.?[0-9]+)$'
    return match(pattern, num) is not None


# операторы и приоритеты
OPERATORS: list[str] = ["+", "-", "*", "/", "^", "%", "#"]
UNARY_OPERATORS: list[str] = ["u-", "u+"]
PRIORITIES: dict = {'+':1, '-':1, '*':2, '/':2, '#': 2, '%':2, '^':3, 'u+':4, 'u-':4}
