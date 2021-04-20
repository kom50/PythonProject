num = int(input('Enter a number :- '))
s = 0
while num != 0:
    s += num % 10
    num //= 10

print('Sum ', s)
