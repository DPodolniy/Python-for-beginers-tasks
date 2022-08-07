from random import randint


def is_valid(s):
    if s in yes:
        return 'yeah'
    elif s in no:
        return 'nope'
    else:
        return False

def generate_password(length,chars):
    password = ''
    for i in range(length):
        password += chars[randint(0, len(chars))]
    return password

digits, lowercase_letters, uppercase_letters = '0123456789', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation, chars, yes, no = '!#$%&*+-=?@^_', '', ['Да', 'да', 'ДА'], ['Нет', 'нет', 'Нет']
symb7 = ['i', 'L', 'l', '0', 'o', 'O', '1']
print('Добро пожаловать в генератор паролей.\n'
      'Количество паролей для генерации?')
inpt1 = input()
while True:
    if inpt1.isdigit() is True:
        if int(inpt1) > 0:
            inpt1 = int(inpt1)
            break
        else:
            print('А может быть все-таки введем целое число больше нуля?')
            inpt1 = input()
    else:
        print('А может быть все-таки введем целое число больше нуля?')
        inpt1 = input()
print('Длина генерируемых паролей?')
inpt2 = input()
while True:
    if inpt2.isdigit() is True:
        if int(inpt2) > 0:
            inpt2 = int(inpt2)
            break
        else:
            print('А может быть все-таки введем целое число больше нуля?')
            inpt2 = input()
    else:
        print('А может быть все-таки введем целое число больше нуля?')
        inpt2 = input()
print('Включать ли цифры?')
inpt3 = input()
while is_valid(inpt3) is False:
    print('Не понимаю, попробуй еще раз')
    inpt3 = input()
if is_valid(inpt3) == 'yeah':
    chars += digits
print('Включать ли прописные буквы?')
inpt4 = input()
while is_valid(inpt4) is False:
    print('Не понимаю, попробуй еще раз')
    inpt4 = input()
if is_valid(inpt4) == 'yeah':
    chars += uppercase_letters
print('Включать ли строчные буквы?')
inpt5 = input()
while is_valid(inpt5) is False:
    print('Не понимаю, попробуй еще раз')
    inpt5 = input()
if is_valid(inpt5) == 'yeah':
    chars += lowercase_letters
print('Включать ли символы?')
inpt6 = input()
while is_valid(inpt6) is False:
    print('Не понимаю, попробуй еще раз')
    inpt6 = input()
if is_valid(inpt6) == 'yeah':
    chars += punctuation
print('Исключать ли неоднозначные символы il1Lo0O?')
inpt7 = input()
while is_valid(inpt7) is False:
    print('Не понимаю, попробуй еще раз')
    inpt7 = input()
if is_valid(inpt7) == 'yeah':
    for i in range(len(symb7)):
        chars = chars.replace(symb7[i], '')

for i in range(inpt1):
    print(generate_password(inpt2, chars))