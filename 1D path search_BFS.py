#起始位置为N，规定下一步走法函数为 f1|f2|f3|...，求最少需要多少步才能到达K及路径
N = 3
K = 114514

def f1(x):
    return x-1

def f2(x):
    return x+1

def f3(x):
    return 2*x

f_all=[f1,f2,f3]

Max_iteration = 100000
layers = []
visited = set()
layers.append([N])
visited.add(N)

connections = {}  # 使用字典表示，键为节点，值为父节点

for i in range(Max_iteration):
    if K == N:
        print("0 step to reach")
        break

    next_layer = set()
    for vertex in layers[i]:
        for f in f_all:
            f_vertex = f(vertex)
            if f_vertex not in visited:
                next_layer.add(f_vertex)
                visited.add(f_vertex)
                connections[f_vertex] = vertex  # 记录节点的父节点
    layers.append(list(next_layer))
    if K in next_layer:
        print(f"{i+1} step to reach")
        break

# 输出路径
path = [K]
while path[-1] != N:
    path.append(connections[path[-1]])
path.reverse()
print("Path:", path)