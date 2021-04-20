# print Nth fibonacci series using loop
def fibonacci_series(num):
    a, b, c = 0, 1, 0
    for i in range(num):
        print(c, end=' ')
        c = a + b
        b, a = a, c


# print fibonacci series using recursive function
def fibonacci_series1(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci_series1(num - 1) + fibonacci_series1(num - 2)


# 1st function
fibonacci_series(5)

print()

# snd function
for i in range(9):
    print(fibonacci_series1(i), end=' ')