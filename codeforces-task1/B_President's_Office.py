'''
    https://codeforces.com/contest/6/problem/B
'''
n,m,c = list(map(str,input().split()))
n,m= int(n),int(m)
matrix=[list(input())[:m] for _ in range(n)]
resultmat=[]
for i in range (n):
    for j in range (m):
        if matrix[i][j]==c :
            if i-1 >=0:
                resultmat.append(matrix[i-1][j])
            if i+1 <n:
                resultmat.append(matrix[i+1][j])
            if j-1 >=0:
                resultmat.append(matrix[i][j-1])
            if j+1 <m:
                resultmat.append(matrix[i][j+1])
resultmat=set(resultmat)
resultmat.discard('.')
resultmat.discard(c)
print (len(resultmat))
