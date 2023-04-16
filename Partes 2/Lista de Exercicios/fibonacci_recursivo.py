def fibonacci(n):
    if n < 1:
        return abs(n)
    else:
        return fibonacci(n-1) + fibonacci(n-2)