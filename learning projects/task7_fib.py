def fib(last):
    x = last if last <= 1 else fib(last-1) + fib(last-2)
    return x
count = int(input("how many fibonacci numbers to show?\n"))
print([fib(i) for i in range(count)], sep = ", " )