# recursive
def fibo(n):

    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

# iterative
def fibo_iter(n, cache = dict()):

    if n == 1 or n == 2:
        return 1

    if n in cache:
        return cache[n]

    cache[n] = fibo_iter(n-1, cache) + fibo_iter(n-2, cache)

    return cache[n]

for i in range(1, 11):
    print(fibo(i))

for i in range(1, 11):
    print(fibo_iter(i))

