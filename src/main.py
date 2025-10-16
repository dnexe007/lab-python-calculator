from src.calculator_runner import run_calculator


def main() -> None:
    """
    Функция для запуска программы пользователем
    :return: Ничего не возвращает
    """
    while True:
        expression = input("enter expression or press enter to quit: ")

        if expression.replace(" ", "") == "":
            print("goodbye:)")
            break

        result = run_calculator(expression)
        if result % 1 == 0:
            result = int(result)

        print("result: ", result)


if __name__ == "__main__":
    main()
