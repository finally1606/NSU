#1
numbers = []
while True:
    num = int(input())
    numbers.append(num)
    if num == -1:
        break
print(max(numbers[:-1]))  # Исключаем -1 из поиска максимума

#2
values = []
while True:
    value = int(input())
    if value == -1:
        break
    values.append(value)
print(len(values))

#3
incomes = []
while True:
    amount = int(input())
    if amount == 0:
        break
    incomes.append(amount)
average = sum(incomes) / len(incomes)
print(average)

#4
n = int(input('Введите целое число: '))
for i in range(1, n + 1):
    triangular_num = i * (i + 1) // 2
    print(triangular_num)

#5
def sum_of_proper_divisors(n):
    return sum(i for i in range(1, n) if n % i == 0)

limit = int(input())
perfect_count = sum(1 for i in range(1, limit)
                if i == sum_of_proper_divisors(i))
print(perfect_count)

#6
height = int(input())
for i in range(1, height + 1):
    print(' ' * (height - i) + '*' * i)

#7
while True:
    s = input('Введите число: ')
    if s.isdigit():
        print(f'Введено целое число: {s}')
        break
    print('Ошибка. Попробуйте еще раз.', end=' ')

#8
# Первый паттерн
for i in range(1, 10):
    left = ''.join(str(x) for x in range(1, i + 1))
    right = ''.join(str(x) for x in range(9, 9 - i, -1))
    print(f"{left}*8+{i}={right}")

# Второй паттерн
for i in range(1, 10):
    left = ''.join(str(x) for x in range(1, i + 1))
    right = '1' * i
    print(f"{left}*9+{i+1}={right}")

# Третий паттерн
for i in range(1, 10):
    num = '1' * i
    print(f"{num}*{num}={int(num)**2}")

#9
def is_prime(num):
    if num < 2:
        return False
    return all(num % i != 0 for i in range(2, int(num**0.5) + 1))

upper_bound = int(input())
primes = [i for i in range(1, upper_bound + 1) if is_prime(i)]
print('\n'.join(map(str, primes)))

#10
def is_perfect(num):
    if num < 2:
        return False
    return sum(i for i in range(1, num) if num % i == 0) == num

n = int(input())
perfect_numbers = [i for i in range(1, n) if is_perfect(i)]
print('\n'.join(map(str, perfect_numbers)))