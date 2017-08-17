fib1 = 1
fib2 = 1
sum1 = 0

while fib1 <= 4000000 or fib2 <= 4000000:
    if fib1 % 2 == 0:
        sum1 += fib1
    fib1 += fib2
    if fib2 % 2 == 0:
        sum1 += fib2
    fib2 += fib1

print(sum1)

