import numpy as np

def random_predict(number:int=1, spectrum: tuple=(1, 101)) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(*spectrum) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

def predict_fast(number:int=1, spectrum:tuple=(1, 101)) -> int:
    """Угадываем число быстрее, чем 'random_predict'

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    a, b, count = *spectrum, 0 # задаем стартовые значения счетчика и концов отрезка 

    while True:
        count += 1
        predict_number = (a + b) // 2 # находим середину отрезка
        if number > predict_number: # наше число оказывается правее середины отрезка, тогда двигаем левую границу вправо
            a = predict_number
        elif number < predict_number: # наше число оказывается левее середины отрезка, тогда двигаем правую границу влево
            b = predict_number         
        else:
            break # выход из цикла, если угадали
    return(count)
    
def score_game(random_predict_func, spectrum: tuple=(1, 101)) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(*spectrum, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict_func(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


# RUN
if __name__ == '__main__':
    score_game(predict_fast)
 