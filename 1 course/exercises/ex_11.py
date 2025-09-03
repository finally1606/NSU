#1
f = str(*open('input.txt', 'r'))
fn = open('output.txt', 'w')
fn.write(f.upper())

#2
f = open('input.txt', 'r')

for i in f.readlines():
    if i[0].lower() == 'a':
        print(i)
f.close()

#3
f = open('input.txt', 'r')

for i in f.readlines():
    print(i[0], end='')
f.close()

#4
f = open('input.txt', 'r')

for i in f.readlines():
    if len(i) >= 20:
        print(i)
f.close()

#5
f = open('input.txt', 'r')

for i in f.readlines():
    if len(i) >= 20:
        print(i)
f.close()

#6
f = open('input.txt', 'r').readlines()
fn = open('output.txt', 'w')
print(len(f), f[0][0:-1])
try:
    if len(f)-1 == int(f[0][0:-1]):
        fn.write('YES')
    else:
        fn.write('NO')
except:
    fn.write('ERROR')
fn.close()

#7
f = open('input.txt', 'r')
fn = open('output.txt', 'w')

for i in f:
    if '100' == i:
        pass
    else:
        fn.write(f'{i}')

#8
f = open('input.txt', 'r').readlines()
fn = open('output.txt', 'w')

for i in range(len(f)):
    if '\n' in f[i]:
       f[i] = f[i][0:-1]

fn.write(sum(int(f[0:31]))/31)
fn.write(sum(int(f[31:59]))/28)
fn.write(sum(int(f[59:90]))/31)
fn.write(sum(int(f[90:120]))/30)
fn.write(sum(int(f[120:151]))/31)
fn.write(sum(int(f[151:181]))/30)
fn.write(sum(int(f[181:212]))/31)
fn.write(sum(int(f[212:243]))/31)
fn.write(sum(int(f[243:273]))/30)
fn.write(sum(int(f[273:304]))/31)
fn.write(sum(int(f[304:334]))/30)
fn.write(sum(int(f[334:365]))/31)

#9
import os

f = open('input.txt', 'r').readlines()
fn = open('output.txt', 'w')

for i in range(len(f)):
    if i%2 == 1:
        fn.write(f[i])

os.makedirs('simple', exist_ok = True)
fn.close()
os.replace("output.txt", "simple/output.txt")

#10
import datetime

f = open('input.txt', 'r').readlines()
fn = open('output.txt', 'w')

now = datetime.date(2025, int(list(f[0].split(sep='.'))[0]), int(list(f[0].split(sep='.'))[1]))

lagged = {}
for i in f[2:]:
    lagged[list(i.split())[0]] = datetime.date(2025, int(list(list(i.split())[1].split(sep='.'))[0]), int(list(list(i.split())[1].split(sep='.'))[1]))

for i in range(len(lagged)):
    if now - i > 3 and i.index() > 1000:
        fn.write(i)


print(lagged)
