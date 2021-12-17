with open('input.txt', 'r+') as f:
    data = [line.strip('\n').split(',') for line in f.readlines()]
    f.close
data = [int(p) for p in data[0]]

best = max(data)*len(data) #worst-case scenario

for n in range(min(data), max(data)+1):
    fuel = sum([abs(p-n) for p in data])
    best = min(distance, best)
print(best)
