from src.common import is_number, UNARY_OPERATORS, OPERATORS


def apply_operation(right_num: float, left_num: float, operation: str) -> float:
    """
    Применение бинарной операции
    :param right_num: Число справа
    :param left_num: Число слева
    :param operation: Бинарная операция
    :return: Результат применения операции к числам
    """
    right_num = float(right_num)
    left_num = float(left_num)

    if operation in "%#":
        if right_num % 1 != 0 or left_num % 1 != 0:
            raise ValueError("operations % and # are not supported with float")
        right_num = int(right_num)
        left_num = int(left_num)

    if operation == "+":
        return left_num + right_num
    elif operation == "-":
        return left_num - right_num
    elif operation == "*":
        return left_num * right_num
    elif operation == "/":
        if right_num == 0:
            raise ValueError("division by zero")
        return left_num / right_num
    elif operation == "#":
        if right_num == 0:
            raise ValueError("division by zero")
        return left_num // right_num
    elif operation == "%":
        return left_num % right_num
    elif operation == "^":
        if left_num < 0 and right_num % 1 != 0:
            raise ValueError("negative number with incorrect degree")
        return left_num ** right_num
    else:
        raise ValueError("unknown operation")


def apply_unary_operation(num: float, operation: str) -> float:
    """
    Применение унарной операции
    :param num: Число, над которым будет проводиться операция
    :param operation: Унарная операция
    :return: Результат операции
    """
    num = float(num)
    if operation == "u+":
        return num
    elif operation == "u-":
        return -num
    else:
        raise ValueError("unknown operation")


def calculate(rpn_tokens: list[str]) -> float:
    """
    Вычисление математического выражения в rpn
    :param rpn_tokens: Выражение в rpn (токены)
    :return: Результат
    """
    stack = []

    if len(rpn_tokens) == 1:
        stack.append(float(rpn_tokens[0]))
    else:
        for token in rpn_tokens:
            if is_number(token):
                stack.append(float(token))
            elif token in UNARY_OPERATORS:
                number = stack.pop(-1)
                operation_result = apply_unary_operation(number, token)
                stack.append(operation_result)
            elif token in OPERATORS:
                number1 = stack.pop(-1)
                number2 = stack.pop(-1)
                operation_result = apply_operation(number1, number2, token)
                stack.append(operation_result)

    result = stack[-1]
    #result = round(result, 5)
    return result
