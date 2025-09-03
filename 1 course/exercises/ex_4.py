#1
password = input()
if password == 'пароль':
    print('Проходи!')
else:
    print('Доступ запрещен!')

#2
first = ['Генрих', 'Герц']
print('Какие два слова передал первой радиограммой Александр Попов?')
part_one = input('Первое слово: ')
part_two = input('Второе слово: ')
if first[0] == part_one and first[1] == part_two:
    print('Верно')
else:
    print('Неверно')

#3
print('Как зовут главного персонажа Романов Яна Флеминга о вымышленном секретной разведывательной службы '
      'Великобритании')
name = input('Имя персонажа ')
if name == 'Джеймс Бонд' or 'Бонд Джеймс' or 'Джеймс':
    print('Верно')
else:
    print('Неверно')

#4
question = input('Вы поедете на бал? ')

if question.lower() != 'нет' and question.lower() != 'да':
    print('Верно')
else:
    print('Неверно')

#5
n = int(input())
k = int(input())
if n>k:
    print(k)
elif k>n:
    print(n)
else:
    print(k)

#6
score = list(map(int, input().split(sep=':')))
if score[0] > score[1]: print(1)
elif score[0] < score[1]: print(2)
else: print(0)

#7
high = list(map(int, input().split()))
n = high[0]
for i in high:
    if i > n:
        n = i
print(n)

#8
name = input('Здравствуйте! Как Вас зовут? ')
print(f'Очень приятно, {name.title()}! Меня зовут Марк')
age = int(input('Сколько Вам лет? '))
if age > 81:
    print(f'Да, {name.title()}, Вы старше меня на {age-81} лет')
else:
    print(f'Да, {name.title()}, я старше Вас на {81 - age} лет')
prog = input('Вам нравится программировать? ')
if prog.lower() == 'нет':
    print('Жаль. Я думал, Вы сможете написать интересную программу для меня')
elif prog.lower() == 'да':
    print('Превосходно! Уверен, у Вас получится написать множество интересных и хороших программ')

#9
dog = input('Собака короткошерстной породы? ')
if dog == 'да':
    dog = input('Рост собаки менее 50 см? ')
    if dog == 'да':
        dog = input('У собаки которкий хвост? ')
        if dog == 'да':
            print('английский бульдог')
        elif dog == 'нет':
            dog = input('У собаки длинные уши? ')
            if dog == 'да':
                print('гончая')
            elif dog == 'нет':
                dog = input('У собаки короткое тело? ')
                if dog == 'да':
                    print('мопс')
                elif dog == 'нет':
                    print('чихуахуа')
    elif dog == 'нет':
        dog = input('Собака весит более 50 кг? ')
        if dog == 'да':
            print('датский дог')
        elif dog == 'нет':
            print('фоксхаунд')
elif dog == 'нет':
    dog = input('Рост собаки менее 50 см? ')
    if dog == 'да':
        dog = input('У собаки доброжедательный характер? ')
        if dog == 'да':
            print('кокер-спаниэль')
        elif dog == 'нет':
            print('ирландский сеттер')
    elif dog == 'нет':
        dog = input('У собаки рост менее 70 см? ')
        if dog == 'да':
            dog = input('У собаки длинные уши? ')
            if dog == 'да':
                print('большой вандейский грифон')
            elif dog == 'нет':
                print('колли')
        elif dog == 'нет':
            dog = input('Окрас рыжиц с белыми отметинами? ')
            if dog == 'да':
                print('сенбернар')
            elif dog == 'нет':
                dog = input('Белоснежный окрас? ')
                if dog == 'да':
                    print('ирландский волкодав')
                elif dog == 'нет':
                    print('ньюфаундлед')

#10
machine = int(input())
if machine%2!=1:
    print('да')
else:
    print('нет')
