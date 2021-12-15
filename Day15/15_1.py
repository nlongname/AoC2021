with open('testinput.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    f.close

data = [[int(c) for c in r] for r in data]
width = len(data[0])
length = len(data)

queue = [(0,0)]
weights = {(0,0):0}

i=0
while queue[i] != (width-1, length-1):
    last = queue[i]
    old_weight = weights[queue[i]]
    candidates = [(last[0]-1, last[1]), (last[0]+1, last[1]), (last[0], last[1]-1), (last[0], last[1]+1)]
    candidates = [c for c in candidates if min(c) >= 0 and c[0] < width and c[1] < length]
    for c in candidates:
        new_weight = old_weight + data[c[0]][c[1]]
        if c not in queue:
            queue.append(c)
            weights[c] = new_weight
        elif queue.index(c) > i: #i.e. already waiting in the queue
            weights[c] = min(weights[c], new_weight)
    weights[last] = -1 #easier if we don't remove entirely, just make sure it stays out of the way
    queue.sort(key=lambda x: weights[x])
    i += 1
print(weights[queue[i]])
