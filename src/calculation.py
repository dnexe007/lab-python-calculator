from src.common import is_number, UNARY_OPERATORS, OPERATORS

# применение бинарной операции
def apply_operation(right_num: float, left_num: float, operation: str) -> float:
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
        return left_num / right_num
    elif operation == "#":
        return left_num // right_num
    elif operation == "%":
        return left_num % right_num
    elif operation == "^":
        return left_num ** right_num
    else:
        raise ValueError("unknown operation")

# применение унарной операции
def apply_unary_operation(num: float, operation: str) -> float:
    num = float(num)
    if operation == "u+":
        return num
    elif operation == "u-":
        return -num
    else:
        raise ValueError("unknown operation")

# алгоритм вычисления
def calculate(rpn: list[str]) -> float:
    stack = []

    if len(rpn) == 1:
        stack.append(float(rpn[0]))
    else:
        for token in rpn:
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

    return  result
