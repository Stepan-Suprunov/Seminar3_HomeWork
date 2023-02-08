# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input('Введите длинну массива: '))
A = [1]
for i in range(n-2):
    A.append(int(input('Введите число для записи в массив: ')))
A.append(n)
x = int(input('Введите искомое число X: '))

count = 0
for i in range(len(A)):
    if A[i] == x:
        count += 1

print(f'Искомое число Х встречается {count} раз.')


# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input('Введите длинну массива: '))
A = [1]
for i in range(n-2):
    A.append(int(input('Введите число для записи в массив: ')))
A.append(n)
x = int(input('Введите искомое число X: '))

closest_num = A[0]
count_exist = float('inf')
count_new = 0
for i in range(len(A)):
    if x < A[i]:
        y = x
        while y < A[i]:
            y += 1
            count_new += 1
    elif x > A[i]:
        y = x
        while y > A[i]:
            y -= 1
            count_new += 1
    else:
        closest_num = A[i]
        break

    if count_new < count_exist:
        count_exist = count_new
        closest_num = A[i]
    count_new = 0

print(closest_num)


# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.

scrab_1 = ('a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r', 'а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т',)
scrab_2 = ('d', 'g', 'д', 'к', 'л', 'м', 'п', 'у',)
scrab_3 = ('b', 'c', 'm', 'p', 'б', 'г', 'ё', 'ь', 'я',)
scrab_4 = ('f', 'h', 'v', 'w', 'y', 'й', 'ы',)
scrab_5 = ('k', 'ж', 'з', 'х', 'ц', 'ч',)
scrab_8 = ('j', 'x', 'ш', 'э', 'ю',)
scrab_10 = ('q', 'z', 'ф', 'щ', 'ъ',)

n = str(input('Введите слово: '))
count = 0
for i in range(len(n)):
    for j in range(len(scrab_1)):
        if n[i] == scrab_1[j]:
            count += 1
    for j in range(len(scrab_2)):
        if n[i] == scrab_2[j]:
            count += 2
    for j in range(len(scrab_3)):
        if n[i] == scrab_3[j]:
            count += 3
    for j in range(len(scrab_4)):
        if n[i] == scrab_4[j]:
            count += 4
    for j in range(len(scrab_5)):
        if n[i] == scrab_5[j]:
            count += 5
    for j in range(len(scrab_8)):
        if n[i] == scrab_8[j]:
            count += 8
    for j in range(len(scrab_10)):
        if n[i] == scrab_10[j]:
            count += 10

print(count)
