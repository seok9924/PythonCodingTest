


input=[73,74,75,71,69,72,76,73]

answer=[0 for i in range(len(input))]

stack=[]
for cur_day, cur_temp in enumerate(input):
    while stack and stack[-1][1] <cur_temp:
        prev_day,_ = stack.pop()
        answer[prev_day] =cur_day-prev_day

    stack.append((cur_day,cur_temp))

print(answer)
