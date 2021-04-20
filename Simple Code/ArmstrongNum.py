# Check a number is armstrong or not
def is_armstrong(num):
    digits, n = 0, num
    # count digits
    while n != 0:
        digits += 1
        n //= 10

    sum1, n = 0, num
    while n != 0:
        sum1 += (n % 10) ** digits
        n //= 10

    if sum1 == num:
        print(num, 'is armstrong no.')
    else:
        print(num, 'is not armstrong no.')
# End function

# call is_armstrong() function


is_armstrong(153)