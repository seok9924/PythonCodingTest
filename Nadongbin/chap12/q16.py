from collections import deque


n,m= map(int,input().split())

data=[]
for i in range(n):
    data.append(input().split())
temp=[[0]*m for _ in range(n)]
def dfs(x,y):
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny]:
                temp[nx][ny]=2
                dfs(nx,ny)

def get_score():
    score= 0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score+=1
    return score

def pillar(count):
    global result
    if count==3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=data[i][j]
        for i in range(n):
            for j in range(m):
                temp[i][j]==2
                dfs(i,j)

    result=max(result,get_score())
    return
    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                data[i][j]=1
                count+=1
                pillar(count)
                data[i][j]=0
                count-=1
pillar(0)
print(result)