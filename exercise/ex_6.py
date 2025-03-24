import math

#1
carpet = list(map(int, input().split("x")))
a, b = carpet[0], carpet[1]

circle_diameter = 2 * 6.5
diagonal = math.sqrt(a ** 2 + b ** 2)

print("да") if diagonal <= circle_diameter else print("нет")

#2
square = list(map(int, input().split("x")))
a, b = square[0], square[1]

volume = list(map(int, input().split("x")))
c, d, e = volume[0], volume[1], volume[2]

hole = a * b
brick_1 = c * e
brick_2 = e * d
brick_3 = c * d

print("да") if brick_1 < hole or brick_2 < hole or brick_3 < hole else print("нет")

#3
n, m = map(int, input().split("x"))
k = int(input())

if k < m * n:
    C = 0
    for string in range(1, n):
        if (string * m) >= k and ((n - string) * m) >= (n * m - k):
            C += 1
    for raw in range(1, m):
        if (raw * n) >= k and ((m - raw) * n) >= (n * m - k):
            C += 1
else:
    print(f'Некорректный ввод')

print('Успешно') if C > 0 else print('Неосуществимо')

#4
chess_square = input()
literal, number = chess_square[0], int(chess_square[1])

even = ["b", "d", "f", "h"]
uneven = ["a", "c", "e", "g"]

if literal in even:
    print("белый") if number % 2 != 0 else print("черный")

if literal in uneven:
    print("черный") if number % 2 != 0 else print("белый")

#5
turn = input().split("-")
forward = turn[0]
side = turn[1]

literal_f = forward[0]
number_f = int(forward[1])
literal_s = side[0]
number_s = int(side[1])

if abs(ord(literal_s) - ord(literal_f)) == 1:
    print("верно") if abs(number_s - number_f) == 2 else print("ошибка")

elif abs(ord(literal_s) - ord(literal_f)) == 2:
    print("верно") if abs(number_s - number_f) == 1 else print("ошибка")

else:
    print("ошибка")

#6
import math

data = list(map(int, input().split()))
n, k, m = data[0], data[1], data[2]

minutes = (math.ceil((n * 2) / k)) * m
print(minutes)

#7
k = int(input())
n = 0
m = 0

for i in range(k // 5):
    if (k - (i * 5)) % 7 == 0:
        N = "да"
        break
for j in range(k // 7):
    if (k - (j * 7)) % 5 == 0:
        m = "да"
        break

print("да") if m == "да" or n == "да" else print("нет")

#8
pass

#9
x_1 = float(input('Координаты по Х первой окружности: '))
y_1 = float(input('Координаты по Y первой окружности: '))
r_1 = float(input('Координаты по R первой окружности: '))
x_2 = float(input('Координаты по Х второй окружности: '))
y_2 = float(input('Координаты по Y второй окружности: '))
r_2 = float(input('Координаты по R второй окружности: '))

distance = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)**0.5
if distance > r_1 + r_2:
    print('Окружности лежат одна вне другой, не касаясь')
elif distance < abs(r_1 - r_2):
    print('Одна окружность лежит внутри другой, не касаясь')
elif distance == r_1 + r_2:
    print('Окружности имеют внешнее касание')
elif distance == abs(r_1 - r_2):
    print('Окружности имеют внутреннее касание')
else:
    print('Окружности пересекаются')

#10
pass
