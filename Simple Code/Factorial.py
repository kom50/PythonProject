# find factorial using loop
def fact(num):   # 1st function
    f = 1
    for i in range(1, num + 1):
        f *= i
    return f


# find factorial using recursive function
def fact1(num):   # 2nd function
    if num == 1:
        return 1
    return num * fact1(num - 1)


# 1st function
print('Factorial : ', fact(4))

# 2nd function
print('Factorial : ', fact1(4))
