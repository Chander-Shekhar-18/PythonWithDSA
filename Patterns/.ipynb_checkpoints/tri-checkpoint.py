n = int(input('Enter the number of rows : '))

for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end=' ')
    for k in range(i, 2 * i):
        print(k, end=' ')
    for l in range(2 * i - 2, i - 1, -1):
        print(l, end=' ')
    print()
