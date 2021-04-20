# Find HCF
def hcf(num1, num2):
    i = 2
    hcf1 = 1
    while num1 > 1 and num2 > 1:
        if num1 % i == 0 and num2 % i == 0:
            hcf1 *= i
            num1 //= i
            num2 //= i
        else:
            i += 1
    return hcf1


# find HCF


print('HCF : ', hcf(4, 16))
