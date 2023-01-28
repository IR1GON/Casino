from time import sleep
from random import randint

stawka = 0
num = [1, 2, 3, 0, 0, 0]
num1 = num[0] = randint(1, 3)
num2 = num[1] = randint(1, 3)
num3 = num[2] = randint(1, 3)
num4 = num[3] = randint(1, 3)
num5 = num[4] = randint(1, 3)
num6 = num[5] = randint(1, 3)
qweshen = input('Хотите сыграть в казино?').lower()
while qweshen != 'нет':
    if qweshen == 'да':
        take_mode = input('Выберети режим с 3,4,5 или 6 числами(для выбора напишите число которое выбрали)')
        if take_mode == '3':
            print(
                'Правила: вы ставите ставку и если 3 числа одинаковые х2 куш,если проиграли минус половина вашей ставки')
            while stawka != 'стоп' or qweshen != 'нет':
                num1 = num[0] = randint(1, 3)
                num2 = num[1] = randint(1, 3)
                num3 = num[2] = randint(1, 3)
                print('На ващем счету:', stawka)
                stawka = int(input('Сколько ставите?(стоп-закончить )'))
                print('Ставки приняты', stawka)
                print(num1)
                sleep(1)
                print(num2)
                sleep(1)
                print(num3)
                if num1 == num2 and num2 == num3:
                    print('Поздровляю вы выйграли, вы получаете', stawka * 2)
                else:
                    qweshen = input('Вы проиграли, продолжить?').lower()
                    if qweshen == 'нет':
                        print('Ваш счет:', stawka / 2)
                        exit(0)
        elif take_mode == '4':
            print(
                'Правила: вы ставите ставку и если 4 числа одинаковые х3 куш,если проиграли минус половина вашей ставки')
            while stawka != 'стоп' or qweshen != 'нет':
                num1 = num[0] = randint(1, 3)
                num2 = num[1] = randint(1, 3)
                num3 = num[2] = randint(1, 3)
                num4 = num[3] = randint(1, 3)
                print('На ващем счету:', stawka)
                stawka = int(input('Сколько ставите?(стоп-закончить )'))
                print('Ставки приняты', stawka)
                print(num1)
                sleep(1)
                print(num2)
                sleep(1)
                print(num3)
                sleep(1)
                print(num4)
                if num1 == num2 and num2 == num3:
                    print('Поздровляю вы выйграли, вы получаете', stawka * 3)
                else:
                    qweshen = input('Вы проиграли, продолжить?').lower()
                    if qweshen == 'нет':
                        print('Ваш счет:', stawka / 2)
                        exit(0)
        elif take_mode == '5':
            print(
                'Правила: вы ставите ставку и если 5 числа одинаковые х4 куш,если проиграли минус половина вашей ставки')
            while stawka != 'стоп' or qweshen != 'нет':
                num1 = num[0] = randint(1, 3)
                num2 = num[1] = randint(1, 3)
                num3 = num[2] = randint(1, 3)
                num4 = num[3] = randint(1, 3)
                num5 = num[4] = randint(1, 3)
                print('На ващем счету:', stawka)
                stawka = int(input('Сколько ставите?(стоп-закончить )'))
                print('Ставки приняты', stawka)
                print(num1)
                sleep(1)
                print(num2)
                sleep(1)
                print(num3)
                sleep(1)
                print(num4)
                sleep(1)
                print(num5)
                if num1 == num2 and num2 == num3:
                    print('Поздровляю вы выйграли, вы получаете', stawka * 4)
                else:
                    qweshen = input('Вы проиграли, продолжить?').lower()
                    if qweshen == 'нет':
                        print('Ваш счет:', stawka / 2)
                        exit(0)
        elif take_mode == '6':
            print(
                'Правила: вы ставите ставку и если 6 числа одинаковые х5 куш,если проиграли минус половина вашей ставки')
            while stawka != 'стоп' or qweshen != 'нет':
                num1 = num[0] = randint(1, 3)
                num2 = num[1] = randint(1, 3)
                num3 = num[2] = randint(1, 3)
                num4 = num[3] = randint(1, 3)
                num5 = num[4] = randint(1, 3)
                print('На ващем счету:', stawka)
                stawka = int(input('Сколько ставите?(стоп-закончить )'))
                print('Ставки приняты', stawka)
                print(num1)
                sleep(1)
                print(num2)
                sleep(1)
                print(num3)
                sleep(1)
                print(num4)
                sleep(1)
                print(num5)
                sleep(1)
                print(num6)
                if num1 == num2 and num2 == num3:
                    print('Поздровляю вы выйграли, вы получаете', stawka * 6)
                else:
                    qweshen = input('Вы проиграли, продолжить?').lower()
                    if qweshen == 'нет':
                        print('Ваш счет:', stawka / 2)
                        exit(0)
