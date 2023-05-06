
n= int(input())

board=[list(map(int,input().split())) for _ in range(n) ]


rminus=0
rzero=0
rplus=0


def dfs(x,y,n):
    global  rplus,rzero,rminus

    num_check=board[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if board[i][j]!=num_check:
                for k in range(3):
                    for l in range(3):
                        dfs(x+k*n//3,y+l*n//3,n//3)
                return
    if num_check==-1:
        rminus+=1
    elif num_check==0:
        rzero+=1
    else:
        rplus+=1

dfs(0,0,n)
print(rminus)
print(rzero)
print(rplus)