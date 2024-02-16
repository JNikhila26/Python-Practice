numRows = 5
#Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
ans = []
for i in range(numRows):
    row = [1] * (i + 1)
    #print(row)
    for j in range(1, i):
        row[j] = ans[i - 1][j] + ans[i - 1][j - 1]
        ans.append(row)
    print(ans)