# perfect number in python
def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum is num:
        return True
    else:
        return False

# Call is_perfect() function
num = int(input('Enter a number :- '))
if is_perfect(num):
    print(num, ' is perfect number.')
else:
    print(num, ' is not perfect number.')