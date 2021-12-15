with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    f.close

#this setup is the absolute worst, but it works
data = [[int(c) for c in r]+[int(c)%9+1 for c in r]+[(int(c)+1)%9+1 for c in r]+[(int(c)+2)%9+1 for c in r]+[(int(c)+3)%9+1 for c in r] for r in data]
data = data + [[c%9+1 for c in r] for r in data] + [[(c+1)%9+1 for c in r] for r in data] + [[(c+2)%9+1 for c in r] for r in data] + [[(c+3)%9+1 for c in r] for r in data]

width = len(data[0])
length = len(data)

queue = [(0,0)]
weights = {(0,0):0}

done = set() #set of points that have been cleared completely, speeds things up considerably to separate them out

while queue[0] != (width-1, length-1):
    last = queue[0]
    old_weight = weights[last]
    candidates = [(last[0]-1, last[1]), (last[0]+1, last[1]), (last[0], last[1]-1), (last[0], last[1]+1)]
    candidates = [c for c in candidates if min(c) >= 0 and c[0] < width and c[1] < length and c not in done]
    for c in candidates:
        new_weight = old_weight + data[c[0]][c[1]]
        if c not in queue:
            queue.append(c)
            weights[c] = new_weight
        else:
            weights[c] = min(weights[c], new_weight)
    done.add(last)
    queue.remove(last)
    queue.sort(key=lambda x: weights[x])
print(weights[queue[0]])
