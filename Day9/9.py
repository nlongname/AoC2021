with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    f.close

data = [[int(n) for n in line] for line in data]

width = len(data[0])
length = len(data)
risk_sum = 0
basins = 0
for x in range(width):
    for y in range(length):
        height = data[y][x]
        candidates = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        candidates = [c for c in candidates if c[0]>=0 and c[0]<width and c[1]>=0 and c[1]<length]
        low_point = sum([data[c[1]][c[0]] > height for c in candidates])//len(candidates)
        if low_point:
            risk_sum += height+1
            basins += 1
print(risk_sum)
