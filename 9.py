for i in range(1,999):
    for j in range(i,999-i):
        c = j ** 2 + i ** 2
        if c ** 0.5 == int(c ** 0.5):
            if i + j + c ** 0.5 == 1000:
                print(i * j * (c ** 0.5))

