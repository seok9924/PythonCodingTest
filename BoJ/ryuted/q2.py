def solution(arr, flag):
    a = []
    for i, v in enumerate(arr):
        if flag[i]:
            a.append(v)
            a.append(v)

        else:
            for i in range(v):
                a.pop()
    return a

arr=[3, 2, 4, 1, 3]
flag=[True, False, True, False, False]

solution(arr,flag)