def is_prime(num):
    i = 2
    while i <= num // 2:
        if num % i == 0:
            return False
        i += 1
    return True


#  Call is_prime() function
n = int(input('Enter a number : '))
if is_prime(n):
    print(n, 'is a prime no.')
else:
    print(n, 'is not a prime no.')