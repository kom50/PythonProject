def is_palindrome(num):
    rev = 0
    n = num
    while num != 0:
        rev = rev * 10 + num % 10
        num //= 10
    # end while loop
    if rev == n:
        return True
    else:
        return False
    

# call is_palindrome() function

num1 = 121
if is_palindrome(num1):
    print(num1, " is Palindrome no.")
else:
    print(num1, ' not palindrome no.')