import random
import math


#Функция
#В которой описана сама игра
#и происходит
#1 - выбор псевдослучайного числа
#2 - шагометр
def play():
    comp_num = random.randint(1, gen)
    step = 0
    while True:
        my_num = int(input('Введите ваше число:\t'))
        if my_num < comp_num:
            print('Ваше число МЕНЬШЕ\n')
            step += 1
            continue
        if my_num > comp_num:
            print('Ваше число БОЛЬШЕ\n')
            step += 1
            continue
        else:
            print('Браво!'
                  'Было загаданно именно {}\n'.format(comp_num))
            print('Вы сделали {} шагов'.format(step))
            stepik(step)
            print('Еще разок?\n')
            break


#Функция
#для выбора действий
def answer():
    while True:
        print('*команды*[ИГРА\КОМП\ВЫХОД]')
        comand = input('Введите команду\n').lower()
        if comand == 'игра':
            play()
        elif comand == 'комп':
            computer()
        elif comand == 'выход':
            print('Вы вышли из игры')
            break
        else:
            print('Вы ввели неверную команду, повторите еще раз!\n')


#Функция
#в которой
#описана игра компьютера
#на основе
#бинарного поиска
def computer():
    comp_num = random.randint(1, gen)
    step = 1
    mass = []

    for i in range(1, gen + 1):
        mass.append(i)
    #print(mass)
    low = 0
    high = len(mass) - 1

    while low <= high:
        middle = (low + high) // 2
        guess = mass[middle]
        print('число: {}'.format(guess))
        if guess == comp_num:
            print('Значение найдено. Было загаданно число: {}'.format(comp_num))
            print('Количество шагов: {}\n'.format(step))
            break
        if guess > comp_num:
            print('Меньше\n')
            high = middle - 1
            step += 1
        else:
            print('Больше\n')
            low = middle + 1
            step += 1


#Функция
#шагометр
def stepik(step):
    if step > log:
        print('А это на {} шагов больше максимума компьютера'.format(step - log))
    else:
        print('Молодец!')


#Основной код
gen = int(input('Введите промежуток от 1 до ... \n'))
print('Компьютер задумал число в промежутке от 1 до {}'.format(gen))
log = math.ceil(math.log(gen, 2))
if log == 0 or log == 1:
    log += 1
print('Компьютеру понадобится не более {} шагов для нахождения задуманного числа'.format(log))
print('А за сколько это сделаешь ты?\n'
      'Хочешь проверить свои силы или посмотреть как это сделает компьютер?\n')
answer()
