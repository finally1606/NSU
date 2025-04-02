#1
price = int(input())
print(str(price)[-3])

#2
time = int(input())
seconds = time%60
minutes = (time % 3600) // 60
hours = time//3600
print(f'{hours} часов {minutes} минут {seconds} секунд')

#3
print(int(input()) % 2)

#4
X, Y, N = input().split()
total = (int(X) * 100 + int(Y) * int(N))
print(f"{total // 100} руб. {total % 100} коп.")

#5
n = int(input())
up = '(\\___/) '
mid = "(='.'=) "
down = '(")_(") '
print(f'{up * n}\n{mid*n}\n{down*n}')

#6
K, N, R = input().split()
N = int(N)
R = int(R)
number = int(K * N)
result = number * R
print(result)

#7
try:
    raw = input('Enter number:')
    num = int(raw)
    print(num)
except ValueError:
    print('Вы ввели не число')

#8
import math

a = float(input())
b = float(input())
c = float(input())

# Вычисляем углы используя теорему косинусов
one = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
two = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
three = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))

print(f'{one}\n{two}\n{three}')

#9
att, comp, yds, td, int_  = map(int, input().split())
a = ((comp/att)-0.3)*5
b = ((yds/att)-3)*0.25
c = (td/att)*20
d = 2.375-(int_/att)*25
print(((a+b+c+d)/6)*100)

#10
x, y = map(int, input().split())
print(int((x % y == 0) or (y % x == 0)))

#11
time = int(input())
print(f'{time//30} {int((time % 30) // 0.5)}')

#12
import datetime
print(datetime.datetime.now().date())

#13
#13th
s = int(input())
c = int(input())
n = int(input())
print(f'страница {n//(s*c)+1} столбец {(n%(s*c))//s+1} строка {(n-(s*c))%s}')
