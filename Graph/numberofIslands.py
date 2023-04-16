from collections import deque

grid =[
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1'],
]


def numberofislands(matrix):
    number_of_islands=0
    row_length=len(matrix)
    column_length=len(matrix[0])
    visited=[[False]*column_length for _ in range(row_length)]

    def bfs(x,y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited[x][y]=True
        q=deque()
        q.append((x,y))

        while q:
            cur_x,cur_y=q.popleft()
            for i in range(4):
                next_x=cur_x+dx[i]
                next_y=cur_y+dy[i]

                if next_x>=0 and next_y>=0 and next_x<row_length and next_y<column_length:
                    if matrix[next_x][next_y]=="1" and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        q.append((next_x,next_y))

    for x in range(row_length):
        for y in range(column_length):
            if matrix[x][y]=='1' and not visited[x][y]:
                bfs(x,y)
                number_of_islands+=1



    return number_of_islands

print(numberofislands(matrix=grid))