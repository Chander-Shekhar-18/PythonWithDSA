def mazeObstacle(n, m, mat):
    mod = 10 ** 9 + 7

    if mat[0][0] == -1:
        return 0
    
    dp = [ [0 for _ in range(m)] for _ in range(n)]

    for i in range(m):
        if mat[0][i] == 0:
            dp[0][i] = 1
        else:
            break
    
    for i in range(n):
        if mat[i][0] == 0:
            dp[i][0] = 1
        else:
            break
    
    for i in range(1, n):
        for j in range(1, m):
            if mat[i][j] == 0:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod

    return dp[n - 1][m - 1]

if __name__ == '__main__':
    print(mazeObstacle(3, 3, [[0, 0, 0], [0, -1, 0], [0, 0, 0]]))