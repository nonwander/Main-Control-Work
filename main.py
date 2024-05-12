"""Скрипт реализует алгоритм перебора элементов исходного массива и возвращает
новый массив на основании условий фильтра.
"""

DEFAULT_ARRAY: list[str] = [
    "123", "It's", "me", "hello", "world", "python", "is", "awesome", ":-)"
]


def user_input() -> list[str]:
    """Формирует массив из строк, введённых пользователем через консоль

    Returns:
        list[str]: пользовательский массив строк
    """
    initial_array = []
    interrupt_keys: list = ["quit", "exit"]
    user_key: str = input("Использовать массив строк по умолчанию? [y/n]\n")
    is_default: bool = True if user_key == "y" else False
    user_interrupt: bool = False if not is_default else True
    while not user_interrupt:
        new_element: str = input("Enter new element or type 'quit'|'exit' to end: ")
        if new_element in interrupt_keys:
            user_interrupt = True
            continue
        initial_array.append(new_element)
    return initial_array


def main() -> list[str]:
    """Основная функция алгоритма

    Returns:
        list[str]: отфильтрованный массив строк
    """
    initial_array: list = user_input()
    if not initial_array:
        initial_array = DEFAULT_ARRAY
    new_array = []
    for string_element in initial_array:
        if len(string_element) <= 3:
            new_array.append(string_element)
    print(new_array)
    return new_array


if __name__ == "__main__":
    """Точка входа в программу
    """
    print(__doc__)
    main()
