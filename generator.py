def gen_(q):
    next_element = 1
    while True:
        next_element *= q
        yield next_element


gen = gen_(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))