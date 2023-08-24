"""
У вас є поле 4х4 (змінна board) у якій знаходиться списаок із 16-ма елементами. Основний алгоритм знаходиться у файлі fifteen.py.

У допоміжному файлі helper.ry є три функції які потрібно самостійно написати (цункції містять заглушки -- повертають значення за замовчуванням). 

Пам'ятайте, що при виведенні поля 4х4 замість 0 виводиться знак нижнього підкреслювання. 

Найпростіші перевірки містьять assert умови. 
Здати вам потрібно файл helper.py з написаними вами функціями. 
"""


def print_bord(bord):
    """Function return string-board to print"""
    # TODO
    return "15 14 13 12\n11 10  9  8\n 7  6  5  4\n 3  1  2  _"


def try_to_move(bord, choise):
    """Function check is _choise_-int is possible to change
    position with 0-int in the bord. If movement is possible do it.
    """
    # TODO
    return bord


def is_board_completed(bord):
    """Function return True if the numbers in the board are ordered
    with zero at the finish, otherwise False"""
    # TODO
    return False


if __name__ == "__main__":
    assert (
        print_bord([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 1, 0, 2])
        == "15 14 13 12\n11 10  9  8\n 7  6  5  4\n 3  1  _  2"
    )
    assert try_to_move([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 1, 2, 0], 2) == [
        15,
        14,
        13,
        12,
        11,
        10,
        9,
        8,
        7,
        6,
        5,
        4,
        3,
        1,
        0,
        2,
    ]
    assert (
        is_board_completed([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])
        == True
    )
