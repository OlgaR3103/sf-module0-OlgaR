import numpy as np
def score_game(game_core_v2):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v2(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


def game_core_v2(number):
    '''Устанавливаем диапазон'''
    a = 1 #нижняя граница диапазона
    z = 100 #верхняя граница диапазона
    predict = (a + z)//2 #сокращение диапазона 
    count = 1 #счетчик попыток
    
    while number != predict:
        count += 1
        predict = (a + z)//2
        if number > predict: 
            a = predict 
            predict = a + 1
        else:
            z = predict 
            predict = z
            
    return count # выход из цикла, если угадали
score_game(game_core_v2)