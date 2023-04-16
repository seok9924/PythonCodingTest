def dfs_stack(graph,start):
    visited=[start]
    df_list=[start]


    while df_list:
        cur= df_list.pop()
        for i in graph[cur]:
            if i not in visited:
                visited.append(i)
                df_list.append(i)
    return visited

def dfs_recur(graph,cur_v,visited=[]):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            visited=dfs_recur(graph,v,visited)
    return visited