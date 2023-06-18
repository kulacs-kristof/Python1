import random

matrix = []
for i in range(7):
    sor = []
    for j in range(7):
        sor.append(random.randint(1, 99))
    matrix.append(sor)

print('Generált mátrix:')
for sor in matrix:
    sor_str = ""
    for elem in sor:
        sor_str += str(elem) + "\t"
    print(sor_str)

t_matrix = []
for i in range(7):
    sor = []
    for j in range(7):
        sor.append(matrix[j][i])
    t_matrix.append(sor)

print('Transzponált mátrix:')
for sor in t_matrix:
    sor_str = ""
    for elem in sor:
        sor_str += str(elem) + "\t"
    print(sor_str)

min = matrix[0][0]
max = matrix[0][0]
for sor in matrix:
    for elem in sor:
        if elem < min:
            min = elem
        if elem > max:
            max = elem

print(f'Mátrix minimum eleme: {min}')
print(f'Mátrix maximum eleme: {max}')

osszeg1 = 0
for i in range(7):
    osszeg1 += matrix[i][i]
print(f'Főátló: {osszeg1}')

osszeg2 = 0
for i in range(7):
    osszeg2 += matrix[i][6-i]
print(f'Mellékátló: {osszeg2}')