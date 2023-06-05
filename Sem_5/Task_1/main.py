# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711
def fibo(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibo(n - 1) + fibo(n - 2)


num = int(input('enter a number of fibonacci\'s sequence:\n'))
print(fibo(num))
