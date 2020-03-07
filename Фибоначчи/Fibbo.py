def fibbo_position():
    '''
    Поиск числа Фибоначчи в определенной позиции
    input = int
    :return:
    '''
    position = int(input('Введите позицию:\n'))
    if position < 0:
        print('Да ты шооо')
        return print('Try again')
    start = [0, 1]
    for i in range(2, position + 1):
        number = start[i - 2] + start[i - 1]
        start.append(number)
    if position == 0:
        start = [0]
    print('Число Фибоначчи для позиции {} равно:'.format(position))
    print(start[position])
    full(start, ['none :D'])


def fibbo_even_num():
    '''
    Сумма четных чисел Фибонначи до определенного
    числа в последовательности
    input = int
    :return:
    '''
    num = int(input('Введите предел для числа:\n'))
    if num < 0:
        print('Да ты шооо')
        return print('Try again')
    start = [0, 1]
    i = 2
    even_summ = 0
    mass = []
    while True:
        number = start[i - 2] + start[i - 1]
        if number % 2 == 0 and number <= num:
            even_summ += number
            mass.append(number)
        elif number > num:
            break
        start.append(number)
        i += 1
    print('Сумма четных чисел Фибоначчи до числа {} равна:'.format(num))
    print(even_summ)
    full(start, mass)


def fibbo_even_pos():
    '''
    Сумма четных чисел Фибоначчи до
    обозначенной позиции
    input = int
    :return:
    '''
    position = int(input('Введите позицию:\n'))
    if position < 0:
        print('Да ты шооо')
        return print('Try again')
    if position < 0:
        print('Да ты шооо')
        return print('Try again')
    start = [0, 1]
    even_summ = 0
    for i in range(2, position + 1):
        number = start[i - 2] + start[i - 1]
        start.append(number)
    smart = start[::3]
    for i in smart:
        even_summ += i
    print('Сумма четных чисел Фибоначчи до позиции {} равна:'.format(position))
    print(even_summ)
    full(start, smart)


def fibbo_odd_num():
    '''
    Сумма нечетных чисел Фибоначчи до
    определенного числа в последовательности
    input = int
    :return:
    '''
    num = int(input('Введите предел для числа:\n'))
    if num < 0:
        print('Да ты шооо')
        return print('Try again')
    start = [0, 1]
    i = 2
    odd_summ = 0
    mass = []
    while True:
        number = start[i - 2] + start[i - 1]
        if number > num:
            break
        start.append(number)
        i += 1
    for i in start:
        if i % 2 != 0:
            odd_summ += i
            mass.append(i)
    if num == 0:
        odd_summ = 0
    print('Сумма нечетных чисел Фибоначчи до числа {} равна:'.format(num))
    print(odd_summ)
    full(start, mass)


def fibbo_odd_pos():
    '''
    Сумма нечетных чисел Фибоначчи до
    обозначенной позиции
    input = int
    :return:
    '''
    position = int(input('Введите позицию:\n'))
    if position < 0:
        print('Да ты шооо')
        return print('Try again')
    start = [0, 1]
    odd_summ = 0
    for i in range(2, position + 1):
        number = start[i - 2] + start[i - 1]
        start.append(number)
    smart = start[::3]
    wow = start[:]
    for i in smart:
        start.remove(i)
    for num in start:
        odd_summ += num
    if position == 0:
        odd_summ = 0
    print('Сумма нечетных чисел Фибоначчи до позиции {} равна:'.format(position))
    print(odd_summ)
    full(wow, start)


def full(*args, **kwargs):
    '''
    Функция для показа последовательностей
    как основной, так и "обработанной"
    (если такая имеется)
    :param args:
    :param kwargs:
    :return:
    '''
    yes = ['y', 'yes', '+', 'да', 'д']
    no = ['n', 'no', '-', 'нет', 'не', 'н']
    print('***команды***')
    print('ДА = {}'.format(yes))
    print('НЕТ = {}\n'.format(no))
    print('Вы хотите увидеть получившуюся последовательность Фибоначчи?')
    answer_1 = input().lower()
    if answer_1 in yes:
        print(args[0])
    else:
        print('ОК')
    print('А, может, Вы желаете посмотреть "рабочую" последовательность?))')
    answer_2 = input().lower()
    if answer_2 in yes:
        print(args[1])
    else:
        print('Давай дасвидания!11!1')


def main():
    print('Какой Вы сегодня Фибоначчи?')
    print('1 - Поиск элемента по позиции в последовательности')
    print('2 - Сумма четных чисел последовательности до заданного числа')
    print('3 - Сумма четных чисел последовательности до определенной позиции')
    print('4 - Сумма не_четных чисел последовательности до заданного числа')
    print('5 - Сумма не_четных чисел последовательности до определенной позиции')
    print('что-то помимо цифр - Никакой (Выход)')
    answer = input()
    if answer == '1':
        fibbo_position()
    elif answer == '2':
        fibbo_even_num()
    elif answer == '3':
        fibbo_even_pos()
    elif answer == '4':
        fibbo_odd_num()
    elif answer == '5':
        fibbo_odd_pos()
    else:
        print('пока')


if __name__ == '__main__':
    main()
