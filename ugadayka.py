import random
f = open('words.txt',encoding='utf8')
s = [i.rstrip() for i in f.readlines()]
def get_random_word():
    word = random.choice(s)
    return word
def change_char(word, index, new_char):
    return word[:index] + new_char + word[index + 1:]

validkeys = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', '-']
word = get_random_word()
# print(word)
print('ПРАВИЛА:')
print('Пишите по одной букве!')
print('Чтобы игра закончилась, напишите слово целиком!')
print('Чтобы показать все отправленные буквы, напишите - "вывести буквы"')
print('Чтобы сдаться, напишите - "сдаюсь"')
print('')
print('Слово загадано! Пишите буквы')
send_letters = []
slova_helpers = ['вывести буквы', 'сдаюсь']
fl = False
# print(word)
hide_word = '_' * len(word)
print(hide_word)
while fl == False:
    key = (input().lower())
    if key == 'вывести буквы':
        print(*send_letters)
    if key == 'сдаюсь':
        print(word)

    if key not in validkeys and key not in slova_helpers:
        if len(key) > 1: print('Неправильное слово!')
        else:print('Такой буквы нет в алфавите')
    if key == word:
        fl = True
    if key in send_letters:
        print('Буква уже была!')
    if key not in send_letters and key in validkeys:
        send_letters.append(key)
        # print(send_letters)
        if key in word:
            print('буква есть в слове!')
            # for i in range(word.count(key)):
            # hide_word = change_char(hide_word, word.index(key), key)
            for i in range(len(word)):
                if word[i] == key:
                    hide_word = change_char(hide_word, i, key)

        if key not in word:
            print('буквы нет в слове!')
    print(hide_word)
if fl:
    print('слово отгаданно!')