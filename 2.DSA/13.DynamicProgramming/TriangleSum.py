def minimumPathSum(triangle):
    n = len(triangle)

    for i in range(n - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

    return triangle[0][0]


if __name__ == '__main__':
    print(minimumPathSum([[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]]))