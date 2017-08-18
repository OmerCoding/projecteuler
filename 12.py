import time

start = time.time()

n = 1
A = True
num = 0

while A:
    divisors = 0
    count = 2
    n += 1
    tri_num = (n * (n + 1)) / 2
    if tri_num ** 0.5 == int(tri_num ** 0.5):
        count -= 1
    for num in range(2, int((n*(n+1) / 2) ** 0.5) + 1):
        if tri_num % num == 0:
            divisors += 1
    count += (divisors * 2)
    print(tri_num, count, n)
    if count > 500:
        print(tri_num, count, n)
        A = False
        break

elapsed = (time.time() - start)

print("found in %s seconds" % elapsed)

