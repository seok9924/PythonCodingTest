from itertools import combinations
n,m= map(int,input().split())
a=[]
chicken=[]
house=[]
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            house.append((i,j))
        if a[i][j]==2:
            chicken.append((i,j))


#치킨위치 집위치 다 받았고 조합을 해야함

combis=list(combinations(chicken,m))

def chicken_dist(combi):
    result=0

    for hx,hy in house:
        tmp=1e9
        for cx,cy in combi:
            tmp=min(tmp,abs(hx-cx)+abs(hy-cy))
        result+=tmp

    return result

result=1e9
for combi in combis:
    result= min(result,chicken_dist(combi))

print(chicken)