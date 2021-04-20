# calculate reverse number and then return reverse number of given number
def reverse(num):
    rev = 0
    while num != 0:
        rev = 10 * rev + num % 10
        num //= 10
    return rev


# reverse using remainder print remainder only

def reverse1(num):
    while num != 0:
        print(num % 10, end='')
        num //= 10
# reverse() function call


r = reverse(123456)
print('Reverse : ', r)

print()

# call snd reverse function
reverse1(124)
