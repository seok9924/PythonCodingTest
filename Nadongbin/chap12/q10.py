def rotate_a_matrix_by_90(a):
    n=len(a)
    m=len(a[0])

    result=[[0]*n for _ in range(m)] #여기서는 n*m 이 달라질수도 있는 모든 transpose의 가능성을 고려하고있다

    for i in range(n):
        for j in range(m):
            result[j][n-1-i]=a[i][j] #나는 반환값의 0 0 을 넣었고 여기는 이런식 표현

    return result


def check(new_lock):  # 이미 3배로 적용한 것을 체크하는 형식으로 체크함수를 구성하였다
    lock_length=len(new_lock)//3
    for i in range(lock_length,lock_length*2):
        for j in range(lock_length,lock_length*2):
            if new_lock[i][j]!=1:
                return False

    return True


def solution(key,lock):
    n=len(lock)
    m=len(key)

    new_lock=[[0]*(n*3) for i in range(n*3)]

    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n]=lock[i][j]

    for rotation in range(4):
        key=rotate_a_matrix_by_90(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]+=key[i][j]
                if check(new_lock)==True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]-=key[i][j]

    return False