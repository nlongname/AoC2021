with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    f.close

algorithm = data[0]
data = data[2:]
rounds = 50
padding = 2*rounds

def pad(data:list,padding:int) -> list:
    data = ['.'*padding + d + '.'*padding for d in data]
    data = ['.'*len(data[0])]*padding + data + ['.'*len(data[0])]*padding
    return data

def enhance(extended_data:tuple, algorithm:str) -> tuple:
    data, infinite = extended_data
    new_data = [['0']*len(data[0]) for l in range(len(data))]
    for y in range(len(data)):
        for x in range(len(data[0])):
            enhancer = [None]*9
            if y == 0:
                enhancer[0] = infinite
                enhancer[1] = infinite
                enhancer[2] = infinite
            if x == 0:
                enhancer[0] = infinite
                enhancer[3] = infinite
                enhancer[6] = infinite
            if y == len(data)-1:
                enhancer[6] = infinite
                enhancer[7] = infinite
                enhancer[8] = infinite
            if x == len(data[0])-1:
                enhancer[2] = infinite
                enhancer[5] = infinite
                enhancer[8] = infinite
            for i,e in enumerate(enhancer):
                if e == None:
                    row = i//3 - 1
                    column = i%3 - 1
                    enhancer[i] = data[y+row][x+column]
            enhancer = ''.join(enhancer)
            new_data[y][x] = algorithm[int(enhancer,2)]
            test = algorithm[int(''.join([infinite]*9),2)]
            if test == '#':
                new_infinite = '1'
            else:
                new_infinite = '0'
    return (new_data, new_infinite)
                

data = pad(data,padding)
infinite = '0'
for r in range(rounds):
    data = [['0' if c== '.' else '1' for c in l] for l in data]
    data, infinite = enhance((data,infinite),algorithm)

#strip padding as needed
while data[0].count('#') == 0:
    data = data[1:]
while data[-1].count('#') == 0:
    data = data[:-1]
left = min([l.index('#') for l in data])
right = min([l[::-1].index('#') for l in data])
data = [l[left:-right] for l in data]

for l in data:
    print(''.join(l))
print(sum([l.count('#') for l in data]))
