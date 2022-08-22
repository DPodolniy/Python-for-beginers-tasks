def caesar_cipher(lang, k, text):
    result, dict = [], ''
    dictionary_lower, dictionary_upper = '', ''
    if lang == 1:
        dictionary_lower, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"
    elif lang == 2:
        dictionary_lower, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLNOPQRSTUVWXYZ"
    for c in range(len(text)):
        if text[c] in dictionary_lower:
            dict = dictionary_lower
        elif text[c] in dictionary_upper:
            dict = dictionary_upper
        else:
            result.append(text[c])
        if text[c] in dict:
            for i in range(len(dict)):
                if 0 <= i + k < len(dict) and text[c] == dict[i]:
                    result.append(dict[i+k])
                elif i + k >= len(dict) and text[c] == dict[i]:
                    result.append(dict[(1 - i - k) % (len(dict) - 1)])
                elif i + k < 0 and text[c] == dict[i]:
                    result.append(dict[(i + k) % len(dict)])
    return ''.join(result)
print('Выберите язык, где 1 - русский, а 2 - английский')
a = int(input())
print('Введите ключ сдвига')
key = int(input())
print('Введите шифруемый текст')
text = input()
print(caesar_cipher(a, key, text))