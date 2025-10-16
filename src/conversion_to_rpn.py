from src.common import is_number, PRIORITIES


def to_rpn(tokens: list[str]) -> list[str]:
    """
    Перевод из инфиксной записи в rpn
    :param tokens: Выражение в инфиксной системе (токены)
    :return: Выражение в rpn (токены)
    """
    rpn_tokens = []
    stack = []

    # перебор токенов
    for token in tokens:
        # для числа
        if is_number(token):
            rpn_tokens.append(token)
        # для открывающей скобки
        elif token == "(":
            stack.append(token)
        # для закрывающей скобки
        elif token == ")":
            while True:
                el = stack.pop(-1)
                if el != "(":
                    rpn_tokens.append(el)
                else:
                    break
        # для оператора
        else:
            # для оператора степени
            if token != "^":
                while (stack and stack[-1] != "(" and
                       PRIORITIES[stack[-1]] >= PRIORITIES[token]):
                    rpn_tokens.append(stack.pop(-1))
            # для остальных операторов
            else:
                while (stack and stack[-1] != "(" and
                       PRIORITIES[stack[-1]] > PRIORITIES[token]):
                    rpn_tokens.append(stack.pop(-1))
            stack.append(token)

    while stack:
        rpn_tokens.append(stack.pop(-1))

    return rpn_tokens
