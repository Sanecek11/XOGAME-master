from typing import Union, Optional

EMPTY_CELL = "_"


def init_field(size: int, empty_cell: str = EMPTY_CELL) -> list[list]:
    """
    Создаёт и возвращет пустое поле для игры

    :param size: размер поля
    :param empty_cell: чем заполняется пустая ячейка
    :return: отображение пустого поля в виде листа листов

    """
    return[[empty_cell] * size for _ in range(size)]


def draw_field(field):
    """
    Функция рисует поле
    :param field: Объект поля
    :return: None
    """
    for row in field:
        print(" ".join(row))


def get_int_val(text: str, border: tuple[int, int] = None) -> int:
    """
    Проверяет и возвращает число (это может быть необходимо когда вы хотите проверить,
        что пользователь ввел именно число и это число лежит в диапазоне border[0] и border[1]).
        Спрашиваем у пользователя ввод числа с текстом text и проверяем что оно соответствует требованиям, если не
        соответствует хотя бы одному требованию, то заново просим ввести число.

    :param text: Текст перед получением числа
    :param border: Ограничение на число (минимум, максимум)
    :return: Возвращает число, которое ввёл пользователь и прошедшее все проверки
    """
    while True:
        try:
            value = int(input(text))
            if border is not None and (value < border[0] or value > border[1]):
                print(f"Введите число от {border[0]} до {border[1]}")
            else:
                return value
        except ValueError:
            print("Введите число")


def get_char_val(text: str, req_list: list) -> str:
    """
    Проверяет и возвращает строку из необходимого списка элементов (req_list).
    Спрашиваем у пользователя ввод строку с текстом text и проверяем что оно соответствует требованиям, если не
       соответствует хотя бы одному требованию, то заново просим ввести строку.

    :param text: Текст перед получением числа
    :param req_list: Ограничение на число
    :return: Строка
    """
    while True:
        value = input(text)
        if value in req_list:
            return value
        else:
            print(f"Введите одно из значений: {req_list}")


def get_index_from_table(field, size: int):
    """
    Получаем индексы куда можем поставить символ игрока.
    Спрашиваем у пользователя куда он хочет поставить, проверяем свободна ли ячейка, если занята,
    то просим заново выбрать куда поставить
    :param field:
    :param size:
    :return: Возвращаем индекс ячейки куда поставил пользователь
    """
    while True:
        x = get_int_val("Введите номер строки (от 0 до {})".format(size - 1))
        y = get_int_val("Введите номер столбца (от 0 до {})".format(size - 1))
        if field[x][y] == EMPTY_CELL:
            return x, y
        else:
            print("Эта ячейка уже занята. Попробуйте еще раз.")


def set_player_in_field(field, current_player: str, index_step):
    """
    Ставим игрока на поле. По переданным координатам index_step ставим игрока current_player на поле field
    :param field:
    :param current_player:
    :return: Возвращаем поле с текущим ходом игрока
    """
    x, y = index_step
    field[x][y] = current_player
    return field


def is_win(field, size: int, player: str) -> bool:
    """
    Определяем произошла ли победа. Если на текущем поле выигрышная комбинация, то возвращает True. Если никто не выиграл,
    то возвращаем False
    :param field:
    :param size:
    :param player:
    :return: bool
    """
    # Проверка горизонтальных линий
    for i in range(size):
        if field[i][0] == player and all(field[i][j] == player for j in range(1, size)):
            return True
    # Проверка вертикальных линий
    for i in range(size):
        if field[0][i] == player and all(field[j][i] == player for j in range(1, size)):
            return True
    # Проверка диагонали слева направо
    if field[0][0] == player and all(field[i][i] == player for i in range(1, size)):
        return True

    # Проверка диагонали справа налево
    if field[0][size - 1] == player and all(field[i][size - i - 1] == player for i in range(1, size)):
        return True

    return False


def change_player(current_player: str) -> str:
    """
    Определяет кто ходит следующий
    :param current_player: Текущий игрок
    :return:
    """
    return "X" if current_player == "O" else "O"


def game(player: str, size: int) -> Optional[str]:
    """
    Запускает игру

    :param player: игрок которых ходит первым
    :param size: размер поля
    :return: возвращаем None если ничья или возвращаем игрока кто победил
    """
    field = init_field(size)
    current_player = player
    step = 0
    while step < size*size:
        draw_field(field)
        index_step = get_index_from_table(field, size)
        step += 1
        field = set_player_in_field(field, current_player, index_step)
        if is_win(field, size, current_player):
            draw_field(field)
            print(f"Выиграл игрок {current_player}")
            return field
        current_player = change_player(current_player)
    print("Ничья!")
    return field


def app():
    """
    Запуск приложения игры крестики-нолики
    :return:
    """
    size = get_int_val("Введите размер поля (например, 3 для 3x3 поля): ")
    first_player = get_char_val("Кто будет ходить первым? Введите 'X' или 'O': ", ['X', 'O'])
    if first_player == 'X':
        print(f'Первым ходит {first_player}')
    print(game(first_player, size))


if __name__ == "__main__":
    app()
