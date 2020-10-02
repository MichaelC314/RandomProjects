def fib(num):
    if num <= 2:
        return 1
    return fib(num - 1) + fib(num - 2)

term = int(input("Enter term: "))

print(fib(term))