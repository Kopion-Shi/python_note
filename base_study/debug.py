def add(a):
    if a == 0:
        return 0
    return a + add(a - 1)


print(add(1000))
