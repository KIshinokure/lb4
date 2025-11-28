def gen():
    yield 2
    n = 3
    while True:
        if all(n % p != 0 for p in range(3, int(n**0.5) + 1, 2)):
            yield n
        n += 2

p = gen()
for _ in range(100):
    print(next(p))