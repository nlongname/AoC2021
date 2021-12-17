filename = 'input.txt'
steps = 100

with open(filename, 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    f.close

data = [[int(p) for p in line] for line in data]

width = len(data[0])
length = len(data)

flash = '*'
fix = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,flash:0}

steps = 0
while True:
    data = [[p+1 for p in line] for line in data]
    while sum([sum([p for p in line if p != flash and p > 9]) for line in data])>0:
        for y in range(length):
            for x in range(width):
                if data[y][x] != flash and data[y][x] > 9:
                    data[y][x] = flash
                    candidates = [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
                    candidates = [c for c in candidates if c[0]>=0 and c[0]<length and c[1] >= 0 and c[1]<width]
                    for c in candidates:
                        if data[c[1]][c[0]] != flash:
                            data[c[1]][c[0]] += 1
    data = [[fix[p] for p in line] for line in data]
    steps += 1
    if sum([sum(line) for line in data]) == 0:
        break
print(steps)
