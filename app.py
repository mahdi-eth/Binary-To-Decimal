import math

def to_decimal(n):
    res = 0
    n_tmp = n
    for i in range(len(str(n))):
        r = n_tmp % 10
        res += r * pow(2,i)
        n_tmp = math.floor(n_tmp / 10)
    print(res)


n = abs(int(input("Enter a binary number: ")))
to_decimal(n)