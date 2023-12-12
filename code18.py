def armstrong_num(n):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** 3
        temp = temp // 10
    return sum
n = int(input("Enter a 3 digit number:"))
r = armstrong_num(n)
if n == r:
    print(r," is an Armstrong number")
else:
    print(r,"is not an Armstrong number")
