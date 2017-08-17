prime_list = [2, 3]
num1 = 5
sum_prime = 5

while num1 < 2000000:
    b1 = True
    for num in prime_list:
        if num1 % num == 0:
            b1 = False
            break
    if b1:
        prime_list.append(num1)
        sum_prime += num1
    num1 += 2

print(sum_prime)

