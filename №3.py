#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

a = input("Введите чило - ")
b = a + str(a)
c = b + str(a)
d = int(a) + int(b) + int(c)

print(a)
print(b)
print(c)

print(d)