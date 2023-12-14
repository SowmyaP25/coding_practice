def narcissist_num(n):
    sum = 0
    length = len(n)
    for i in n:
        sum = sum + int(i) ** length
    return sum
n = input("Enter a 4 digit number:")
r = narcissist_num(n)
if int(n) == r:
    print(r," is an narcissist number")
else:
    print(r,"is not an narcissist number")
