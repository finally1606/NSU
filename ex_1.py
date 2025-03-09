#1
print('Hello, Python!\n')

#2
print('Привет, Python!')
print('Hello, Python!')
print('Bonjour, Python!')
print('Hej, Python!')
print('Hola, Python!\n')

#3
print('Привет', 'Python!', sep='\n')

#4
print('(\\___/)')
print('''(='.'=)''')
print('(")_(")\n')

#5
print('Привет, Python!', 'Hello, Python!', 'Bonjour, Python!', 'Hej, Python!', 'Hola, Python!\n', sep='\n')

#6
name = input('Как вас зовут? ')
print(f'Здравствуйте, {name}')

#7
name = input('Как вас зовут? ')
print(f'Здравствуйте, {name}')
hobby = input('Что вам нравится? ')
print(f'Отлично, {hobby} - хорошее увлечение.')

#8
login = 'durov'
password = '12345'
user_entered_login = input('Login: ')
user_entered_password = input('Password: ')

if login !=user_entered_login or password != user_entered_password:
    print('Invalid login or password')
else:
    password = input('New password: ')
    print(f'User {login} has changed password to {password}')

#9
print('Введите плей-лист папы:')
song_1, song_2, song_3, song_4, song_5 = input(), input(), input(), input(), input()
print('Плейлист мамы:', song_5, song_4, song_3, song_2, song_1, sep='\n')

#10
flinght = input('Номер рейса: ')
compny_name_ru = input('Название авиакомпании(на русском языке): ')
compny_name_en = input('Название авиакомпании(на английском языке): ')
arrival_city_ru = input('город прилёта(на руском языке): ')
arrival_city_en = input('город прилёта(на английском языке): ')
print(f'\nЗаканчивается посадка на рейс {flinght} авиакомпании {compny_name_ru} до {arrival_city_ru}')
print(f'This is the final boarding call for {compny_name_en} flight {flinght} to {arrival_city_en}')

#11
name = input('Как вас зовут? ')
print(f'Привет, {name}!')
#12
all = int(input(''))
print((all-4608)/6)

#13
r1 = float(input('Введите первый радиус: '))
r2 = float(input('Введите второй радиус: '))
outer_radius = max(r1, r2)
inner_radius = min(r1, r2)
area = abs(3.14159265358980 * (outer_radius**2 - inner_radius**2))
print(area)

#14
number = int(input())
print(number-4)

#15
metric_cm = float(input())
print(f'{metric_cm/(2.54*12*3)} ярдов')
print(f'{metric_cm/(2.54*12*3*1760)} мили')
print(f'{metric_cm/(2.54*12)} футов')
print(f'{metric_cm/2.54} дюймов')
