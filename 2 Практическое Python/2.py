# умножение двух матриц A (n x m) и B (m x k)
n = int(input("Введите количество строк первой матрицы: "))
m = int(input("Введите количество столбцов первой матрицы (и строк второй): "))
k = int(input("Введите количество столбцов второй матрицы: "))

print("Введите элементы первой матрицы построчно:")
A = []
for i in range(n):
    row = list(map(int, input().split()))
    while len(row) != m:
        print("Нужно ровно", m, "чисел. Введите строку ещё раз:")
        row = list(map(int, input().split()))
    A.append(row)

print("Введите элементы второй матрицы построчно:")
B = []
for i in range(m):
    row = list(map(int, input().split()))
    while len(row) != k:
        print("Нужно ровно", k, "чисел. Введите строку ещё раз:")
        row = list(map(int, input().split()))
    B.append(row)

C = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for t in range(m):
            C[i][j] += A[i][t] * B[t][j]

print("Результирующая матрица:")
for row in C:
    print(*row)
