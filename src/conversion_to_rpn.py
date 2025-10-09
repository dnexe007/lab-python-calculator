from src.common import is_number, PRIORITIES


# алгоритм перевода из инфиксной записи в rpn
def to_rpn(tokens: list[str]) -> list[str]:
    rpn = []
    stack = []

    # перебор токенов
    for token in tokens:
        # для числа
        if is_number(token):
            rpn.append(token)
        # для открывающей скобки
        elif token == "(":
            stack.append(token)
        # для закрывающей скобки
        elif token == ")":
            while True:
                el = stack.pop(-1)
                if el != "(":
                    rpn.append(el)
                else:
                    break
        # для оператора
        else:
            # для оператора степени
            if token != "^":
                while (stack and stack[-1] != "(" and
                       PRIORITIES[stack[-1]] >= PRIORITIES[token]):
                    rpn.append(stack.pop(-1))
            # для остальных операторов
            else:
                while (stack and stack[-1] != "(" and
                       PRIORITIES[stack[-1]] > PRIORITIES[token]):
                    rpn.append(stack.pop(-1))
            stack.append(token)

    while stack:
        rpn.append(stack.pop(-1))

    return rpn
