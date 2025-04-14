# 1
a, b, c = map(int, input().split())
perimeter = 2 * a * c + 2 * b
print(perimeter)

# 2
from math import sqrt
value = int(input())
while value > 2:
    value = sqrt(value)
    print(f'{value:.3f}')

# 3
n = int(input())
for d in range(2, n + 1):
    if n % d == 0:
        print(d)
        break

# 4
nums = []
while True:
    x = int(input())
    nums.append(x)
    if x == 0:
        break
res = sum(1 for item in nums if item % 4 == 0)
print(res)

# 5
results = []
for number in range(100000, 999997):
    s1, s2, s3, s4 = str(number), str(number+1), str(number+2), str(number+3)
    if s1[1] == s1[5] and s1[2] == s1[4] and \
       s2[1] == s2[5] and s2[2] == s2[4] and \
       s3[1] == s3[4] and s3[2] == s3[3] and \
       s4[0] == s4[5] and s4[1] == s4[4] and s4[2] == s4[3]:
        results.append(number)
print(results)

# 6
special = [i**2 for i in range(10, 100) if str(i) in str(i**2) and i**2 < 1000 and i**2 % 100 == i]
print(special)

# 7
from tqdm import tqdm
matches = []
for x in tqdm(range(1000, 10000)):
    sx = str(x)
    for y in range(1000, 10000):
        sy = str(y)
        total = str(x + y)
        if total[3] == sy[3] == sx[1] and \
           total[2] == sx[2] and total[1] == sy[1] and total[0] == sy[0] and \
           total[4] not in sy + sx and \
           sy[2] not in sx + total and \
           sx[0] not in sy + total and sx[3] not in sy + total:
            matches.append([x, y, x + y])
print(matches)

# 8
from math import isqrt
target = int(input())
count = 0
for x in range(isqrt(target) + 1):
    y_squared = target - x * x
    if y_squared >= 0 and int(y_squared**0.5)**2 == y_squared:
        count += 1
print(count // 2)

# 9
from math import factorial
x = int(input())
print(factorial(x + 2) / ((x + 2) / 2))

# 10
from math import factorial as fact

def find_inverse_fact(val):
    acc, i = 1, 1
    while acc < val:
        i += 1
        acc *= i
    return i if acc == val else None

target = int(input())
base = find_inverse_fact(target)
if base is None:
    print("Invalid input")
else:
    items = [base - i for i in range(base - 1)]
    shifts = 0
    idx = len(items)
    while idx > 2:
        items[0] += items[idx - 1]
        items[idx - 1] = 0
        idx -= 1
        shifts += 1
    print(base + shifts)
