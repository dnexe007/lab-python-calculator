from src.common import is_number, OPERATORS
from string import digits

def tokenize(expression: str) -> list[str]:

    tokens: list[str] = []

    opened_brackets  = 0

    current_number = ""

    # добавление current number в токены
    def apply_number():
        nonlocal current_number

        if current_number == "":
            return

        if not is_number(current_number):
            raise ValueError("incorrect number")

        if tokens and (is_number(tokens[-1]) or tokens[-1] == ")"):
            raise ValueError("number in wrong place")

        tokens.append(current_number)
        current_number = ""

    if expression.replace(" ", "") == "":
        raise ValueError("come on, enter something")

    expression = expression.replace(",", ".")
    expression = expression.replace("//", "#")
    expression = expression.replace("**", "^")

    # перебор входной строки
    for i in expression:

        # для цифр
        if i in digits:
            current_number += i

        # для точки
        elif i == ".":
            if "." in current_number:
                raise ValueError("second dot in number")
            current_number += i

        # для операторов и скобок
        else:
            apply_number()

            # для открывающей скобки
            if i == "(":
                if tokens and (is_number(tokens[-1]) or tokens[-1] == ")"):
                    raise ValueError("opening bracket error")
                tokens.append(i)
                opened_brackets += 1

            # для закрывающей скобки
            elif i == ")":
                if (opened_brackets == 0 or
                        (tokens[-1] != ")"and not is_number(tokens[-1]))):
                    raise ValueError("closing bracket error")
                tokens.append(i)
                opened_brackets -= 1

            # для операторов
            elif i in OPERATORS:
                # для унарных операторов
                if (not tokens) or (tokens[-1] == "("):
                    if i not in "+-":
                        raise ValueError("incorrect unary operator")
                    else:
                        tokens.append("u" + i)
                # для остальных операторов
                elif tokens[-1] in OPERATORS:
                    raise ValueError("operator after operator")
                else:
                    tokens.append(i)

            # обнаружение неизвестных символов
            elif i != " ":
                raise ValueError("unknown character")

    apply_number()

    if opened_brackets > 0:
        raise ValueError("missing closing bracket")

    if tokens[-1] in OPERATORS:
        raise ValueError("operator at the end of expression")

    return tokens
