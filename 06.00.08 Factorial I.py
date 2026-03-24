def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

y = 5
x = factorial(y)
print(x)
print(factorial(3))
print(factorial(10))