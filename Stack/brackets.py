s="{{}}"

bracket=[]

for i in s:
    if i =="(":
        bracket.append(")")
    elif i=="{":
        bracket.append("}")
    elif i=="[":
        bracket.append("]")

    elif not bracket or bracket.pop()!= i:
        answer=False

if not bracket:
    answer=True

print(answer)