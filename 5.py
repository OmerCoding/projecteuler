num1 = 1

while 1:
    if num1 % 20 == 0 and num1 % 19 == 0 and num1 % 18 == 0 and num1 % 17 == 0 and num1 % 16 == 0 and num1 % 15 == 0 \
    and num1 % 14 == 0 and num1 % 13 == 0 and num1 % 12 == 0 and num1 % 11 == 0:
        print(num1)
        break
    else:
        num1 += 1
