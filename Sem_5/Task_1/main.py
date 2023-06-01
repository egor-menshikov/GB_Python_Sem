def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
num = int(input('enter a number of fibonacci\'s sequence:\n'))
print(fibo(num))