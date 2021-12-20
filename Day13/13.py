from ast import literal_eval

with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    f.close

instructions = [d for d in data if d.startswith("fold along")]
points = [literal_eval(d) for d in data if d != '' and d not in instructions]
instructions = [d.strip('fold along ').split('=') for d in instructions]
instructions = [[d[0],int(d[1])] for d in instructions]

for i in instructions:
    line=i[1]
    if i[0] == 'x':
        points = list(set([(line-abs(line-p[0]),p[1]) for p in points]))
    else:
        points = list(set([(p[0],line-abs(line-p[1])) for p in points]))

width = max(points, key=lambda p: p[0])[0]+1
length = max(points, key=lambda p: p[1])[1]+1

for y in range(length):
    temp = ''
    for x in range(width):
        if (x,y) in points:
            temp += '#'
        else:
            temp += ' '
    print(temp)
