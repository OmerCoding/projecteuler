def is_palindrome(pali):
    pali = str(pali)
    i = 0
    j = len(pali) - 1
    while i < j:
        if pali[i] != pali[j]:
            return False
        i += 1
        j -= 1
    return True


num1 = 0
for i in range(100,1000):
    for j in range(100,1000):
        if is_palindrome(i * j):
            if i * j > num1:
                num1 = i * j

print(num1)