import pytest

from src.calculator_runner import run_calculator

def test_correct() -> None:
    correct_expressions = {
        # всякое разное
        "1": 1,
        "((1))": 1,
        "-1 + 2 - 3 * 4 / 5" : -1.4,
        "5 * (1 + 3)": 20,
        "2 ^ 3 ^ 2": 512,
        "-(1 + 3)": -4,
        "-3 + 5 * 2 ^ 3 / (4 - 2)": 17,
        "(10 + 2) // 4 + 7 % 3 * (-2)": 1,

        # варианты написания
        "5 // 2": 2,
        "5 # 2": 2,

        "5 ** 2": 25,
        "5 ^ 2": 25,

        "0.5 + 1": 1.5,
        ".5 + 1": 1.5,
        "0,5 + 1": 1.5,
        ",5 + 1": 1.5
    }
    for expr in correct_expressions:
        assert run_calculator(expr) == correct_expressions[expr]


def test_errors() -> None:
    incorrect_expressions = [
        # синтаксические ошибки
        '', '1 + + 3', '* 3 + 1', '1 + 3 +', '1 1 + 3',
        '(1 + 3) 1', '1 (1 + 3)', '1 + 3)', '(1 + 3', '(1 + 3) (1 + 3)',
        '1. + 3', '1 + ()', '1.1.1 + 3', '1a + 3', '1 / / 3',

        # вычислительные ошибки
        '1/0', '1.1 // 2', '1.1 % 2', '-2^2.1'
    ]
    for expr in incorrect_expressions:
        with pytest.raises(ValueError):
            run_calculator(expr)
