num = 600851475143
fac = 0

while num > 1:
    i = 2
    while num % i != 0:
        i += 1
    if i > fac:
        fac = i
    num /= i

print(fac)
