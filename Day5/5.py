with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    f.close

data = [line.split(' -> ') for line in data]
data = [[point.split(',') for point in line] for line in data]
data = [[tuple(int(coordinate) for coordinate in point) for point in line] for line in data]
data = [sorted(line) for line in data]

#limit to vertical or horizontal lines for now
#data = [line for line in data if line[0][0] == line[1][0] or line[0][1] == line[1][1]]

one_line = set()
multiple_lines = set()

for line in data:
    if line[0][0] == line[1][0]:
        for y in range(line[0][1],line[1][1]+1):
            current = (line[0][0],y)
            if current in one_line:
                one_line.remove(current)
                multiple_lines.add(current)
            elif current not in multiple_lines:
                one_line.add(current)
    elif line[0][1] == line[1][1]:
        for x in range(line[0][0],line[1][0]+1):
            current = (x, line[0][1])
            if current in one_line:
                one_line.remove(current)
                multiple_lines.add(current)
            elif current not in multiple_lines:
                one_line.add(current)
    else:
        length = line[1][0]-line[0][0]
        #note: x is always increasing because of how I sorted the points, but y might not be
        y_direction = (line[1][1]-line[0][1])//abs(line[1][1]-line[0][1])
        for a in range(length+1):
            current = (line[0][0]+a, line[0][1]+a*y_direction)
            if current in one_line:
                one_line.remove(current)
                multiple_lines.add(current)
            elif current not in multiple_lines:
                one_line.add(current)
print(len(multiple_lines))
