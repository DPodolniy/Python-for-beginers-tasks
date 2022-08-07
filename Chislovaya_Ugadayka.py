from random import randint


def is_valid(inpt):
    return inpt.isdigit() and 1 <= int(inpt) <= rnum


print('Добро пожаловать в числовую угадайку')
answ = 'y'
while answ == 'y':
    print('Введите целое число в качестве правой границы для загаданного числа')
    rnum = input()
    while rnum.isdigit() is False:
        print('А может быть все-таки введем целое число?')
        rnum = input()
    if rnum.isdigit() is True:
        rnum = int(rnum)
        num, counter = randint(1, rnum), 0
    print('Введите целое число от 1 до', rnum)
    inpt = input()
    while inpt != num:
        counter += 1
        if is_valid(inpt) is True:
            inpt = int(inpt)
            if inpt < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                inpt = input()
                continue
            elif inpt > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
                inpt = input()
                continue
            elif inpt == num:
                print('Вы угадали, поздравляем!')
                break
        elif is_valid(inpt) is False:
            print('А может быть все-таки введем целое число от 1 до 100?')
            inpt = input()
            continue
    print('Количество попыток - ', counter)
    print('Спасибо, что играли в числовую угадайку. Введите "y", чтобы повторить')
    answ = input()
    continue
print('До встречи!')
