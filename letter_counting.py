with open('testLaunch.py') as inf: # выбрать нужный файл
        a = inf.readline().strip()
        print(a)

new_str = ''
count = 0

while len(a) != count:
    letters = a[count]
    count += 1

    number = ''
    while len(a) != count and a[count].isdigit():
        number += a[count]
        count += 1

    new_str += letters * int(number)


print(new_str)

with open('test_wring.txt', 'w') as ouf: # выбрать нужный файл
    ouf.write(new_str)









