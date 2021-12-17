with open('input.txt', 'r+') as f:
    data = [line.strip('\n').split(' ') for line in f.readlines()]
    f.close

data = [line[-4:] for line in data]
data = [[1 for entry in line if len(entry) in [2,3,4,7]] for line in data]
print(sum([sum(line) for line in data]))
