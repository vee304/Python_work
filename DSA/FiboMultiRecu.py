def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

number = 43
fibo_no = fibo(number)
print(fibo_no)

