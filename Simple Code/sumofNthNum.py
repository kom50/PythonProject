# Sum of nth natural numbers
def sum_nth(num):
    s = 0
    for i in range(num + 1):
        s += i
    return s


# find sum of nth odd numbers
def sum_nth_odd(num):
    s = 0
    for i in range(num):
        if i % 2 != 0:
            s += i
    return s


# find sum of nth odd numbers
def sum_nth_even(num):
    s = 0
    for i in range(num):
        if i % 2 == 0:
            s += i
    return s


# call function
print('Sum of nth natural numbers : ', sum_nth(5))

# call sum_nth_odd() function
print('sum of nth odd numbers : ', sum_nth_odd(5))

# call sum_nth_odd() function
print('sum of nth even numbers : ', sum_nth_even(5))


