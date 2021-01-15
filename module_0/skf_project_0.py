import numpy as np


def game_core_v1(number):  # Принимает угадываемое число
    # возвращает число изпользываных попыток для нахождения числа
    first = 1  # -первое число  из заданного диапозона
    last = 100  # -последнее число диапозона
    count = 0
    predicted = 0

    while predicted != number:  # находит число стояще по середине, сравнивает его с угадываемым
        predicted = (first + last) // 2  # в зависимости от '<' или '>' каждый раз убирает половину диапозона
        count += 1  # пока не останется угадываемое число

        if predicted == number:
            return count

        elif predicted < number:
            first = predicted + 1

        elif predicted > number:
            last = predicted - 1


def game_score(game_core):  # принимает функцию, которая угадывает число
    # запускает функцию 1000 раз,сохраняя число исользываных попыток для каждой игры
    count_ls = []  # возвращает среднее значения за все игры и выводит его на экран
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)

    for number in random_array:
        count_ls.append(game_core(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return score


game_score(game_core_v1)
