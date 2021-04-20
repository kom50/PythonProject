# Find LCM
def lcm(num1, num2):
    i = 2
    lcm1 = 1
    while num1 > 1 or num2 > 1:
        if num1 % i == 0 or num2 % i == 0:
            lcm1 *= i
            num1 //= i
            num2 //= i
        else:
            i += 1
    return lcm1


# find LCM

print(lcm(4, 16))
