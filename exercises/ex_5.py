#1
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('366')
else:
    print('365')

#2
import math as m
import turtle as t


def draw_circle(xc, yc, r):
    t.up()
    t.pen(pencolor='orange', pensize=1)
    t.setposition(xc, yc - r)
    t.down()
    t.circle(r)


def draw_dot(x, y):
    t.up()
    t.setposition(x, y)
    t.down()
    t.dot(10, 'black')


def main():
    xc, yc, r = (int(input()) for _ in range(3))
    x, y = (int(input()) for _ in range(2))
    draw_circle(xc, yc, r)
    draw_dot(x, y)
    distance = m.sqrt((xc - x) ** 2 + (yc - y) ** 2)

    if distance > r:
        print('Точка вне окружности')
    elif distance == r:
        print('Точка на окружности')
    else:
        print('Точка внутри окружности')

    t.mainloop()

main()

#3
num = int(input())
if num // 1000 == num % 10 and (num // 100) % 10 == (num // 10) % 10:
    print('Настоящее')
else:
    print('Кривое')

#4
parrot = int(input())
parrot_last = parrot % 10 if parrot > 9 else parrot
match parrot_last:
    case 1:
        print(f'{parrot} попугай')
    case 2 | 3 | 4:
        print(f'{parrot} попугая')
    case _:
        print(f'{parrot} попугаев')

#5
mass_kg = int(input()) * 0.453592
height_m = int(input()) * 0.0254
bmi = round(mass_kg / (height_m ** 2), 2)

if bmi < 16:
    print('Выраженный дефицит массы тела')
elif bmi < 18.5:
    print('Недостаточная масса тела')
elif bmi < 25:
    print('Норма')
elif bmi < 30:
    print('Избыточная масса тела')
elif bmi < 35:
    print('Ожирение первой степени')
elif bmi < 40:
    print('Ожирение второй степени')
else:
    print('Ожирение третьей степени')

#6
values = {int(input()) for _ in range(3)}
print(len(values) if len(values) < 3 else 0)

#7
N, K, M = (int(input()) for _ in range(3))
clockwise_dist = abs(M - K - 1)
print(min(clockwise_dist, N - clockwise_dist))

#8
kn = int(input())
galleons = kn // (17 * 29)
sickles = (kn % (17 * 29)) // 29
knats = kn % 29

if knats == 0 and sickles == 0:
    print(f'{galleons} галеон')
elif knats == 0:
    print(f'{galleons} галеон,\n{sickles} сиклей')
elif sickles == 0:
    print(f'{galleons} галеон,\n{knats} кнатов')
else:
    print(f'{galleons} галеон,\n{sickles} сиклей,\n{knats} кнатов')

#9
heights = list(map(int, input().split()))
heights_sorted = sorted(heights)
print(*heights_sorted)

#10
pin = input()
error_count = 0

if len(pin) > 4:
    error_count += 1

if sum(pin.count(digit) for digit in set(pin)) > 4:
    error_count += 1

if pin.isdigit() and 1900 <= int(pin) <= 2050:
    error_count += 1

print('ERROR' if error_count else 'OK')


