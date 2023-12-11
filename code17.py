def sum_digits(n):
    sum = 0
    while n>0:
        digit = n%10
        sum = sum + digit*digit
        n = n//10
    print('sum of digits',sum)
    return sum
sum_digits(float(input('Enter 3 digit number:')))
