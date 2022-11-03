"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
import random
import numpy as np


def random_predict(number: int = 1) -> int:
    """_summary_

    Args:
        number (int, optional): _description_. Defaults to np.random.randint(1, 101).

    Returns:
        int: _description_
    """
    count = 0
    nmax = 102
    nmin = 1
    
    while True:
        count += 1
        predict_number = (nmin+nmax)//2# предполагаемое число
        if number < predict_number:
            nmax = predict_number
        elif number > predict_number:
            nmin = predict_number
        else:
            number == predict_number
            # print(f'Компьютер угадал загаданное число за {count} попыток. Это число {number}')
            break
    return count
def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
