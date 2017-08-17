prime_list = [2, 3]
prime_num = 2
num1 = 5


while prime_num < 10001:
    b1 = True
    for num in prime_list:
        if num1 % num == 0:
            b1 = False
            break
    if b1:
        prime_num += 1
        prime_list.append(num1)
    num1 += 2

print(prime_list[prime_num - 1])

