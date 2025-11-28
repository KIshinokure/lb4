def my_reduce(func, sequence, initial=None):
    it = iter(sequence)
    value = initial if initial is not None else next(it)
    for item in it:
        value = func(value, item)
    return value

result = my_reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
print(result)