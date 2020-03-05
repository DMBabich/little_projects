import random
import time

# команды
yes = ['y', 'yes', '+', 'да', 'д']
no = ['n', 'no', '-', 'нет', 'не', 'н']


def play():
    card = [i for i in range(2, 12)] * 4  # картеечки
    random.shuffle(card)
    # счет очков
    my_count = 0
    comp_count = 0
    # списки для проверки отрицательного ответа
    quest = []
    my_quest = []
    tour = 1
    while True:
        ##################################
        #             PLAYER             #
        ##################################
        # если было нет, то и хода нет
        if 'no' not in my_quest:
            print('Ход Игрока')
            print('Взять карту?')
            answer = input().lower()
            if answer in yes:
                alfa = card.pop()
                my_count += alfa
                print('Вы взяли карту номиналом {}'.format(alfa))
                print('Ваш счет: {} \n'.format(my_count))
            else:
                my_quest.append('no')
                print('Вы отказались брать карту')
                print('Ваш счет: {}'.format(my_count))

        ##################################
        #           COMPUTER             #
        ##################################

        if 'no' not in quest:
            time.sleep(2)  # компик в раздумьях :D
            print('Ход компьютера\n')
            # betta = random.choice(comp_choise)
            # add logic
            if comp_count not in range(18, 22) and comp_count <= 21:
                comp_card = card.pop()
                print('Компьютер взял карту\n')
                comp_count += comp_card
            elif comp_count >= 25:
                quest.append('no')
                print('Компьютер отказался брать карту\n')
            else:
                quest.append('no')
                print('Компьютер отказался брать карту\n')

        time.sleep(1)  # задержка перед подсчетом
        print('*' * 25)
        print('Закончился {} тур!'.format(tour))
        tour += 1
        print('*' * 25)

        # проверка на нет\нет
        #####################################
        #               RESULT              #
        #####################################
        if 'no' in my_quest and 'no' in quest:
            print('И Вы и компьютер отказались брать карту')
            print('Результаты:')
            print('Ваш счет: {} \n Счет компьютера: {} \n'.format(my_count, comp_count))
            if my_count > 21 and my_count > comp_count:
                print('Вы проиграли\n')
            if my_count == 21 and comp_count != 21:
                print('ВЫ ПОБЕДИЛИ!\n')
            if my_count == 21 and comp_count == 21:
                print('Победила дружба :P\n')
            if 21 < my_count < comp_count:
                print('Вы оказались ближе к 21, Вы победили\n')
            if my_count <= 21 < comp_count:
                print('Компьютер набрал больше 21, Вы победили\n')
            if my_count < comp_count <= 21:
                print('Вы проиграли\n')
            if comp_count < my_count <= 21:
                print('Вы победили \n')
            if my_count <= 21 < comp_count:
                print('Вы победили\n')
            print('конец игры\n \n \n')
            break


while True:
    print('Do you want to play?')
    print('***commands:***')
    print('***{}***'.format(yes))
    print('***{}***'.format(no))
    a = input().lower()
    if a in yes:
        play()
    elif a in no:
        print('bye bye, see you later')
        break
    else:
        print('Вы ошиблись при вводе, попробуйте еще разок')

'''
DELETE ME!
Теперь игра по правилам,
(мы так в детстве играли :D )
а именно:
берется последняя карта
Также добавлена небольшая
логика компьютеру
'''
