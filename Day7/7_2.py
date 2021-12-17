with open('input.txt', 'r+') as f:
    data = [line.strip('\n').split(',') for line in f.readlines()]
    f.close
data = [int(p) for p in data[0]]

best = sum([(p*(p+1))//2 for p in data]) #0-case, to get started, since worst-case is more complicated

for n in range(1, max(data)+1):
    fuel = sum([(abs(p-n)*(abs(p-n)+1))//2 for p in data])
    best = min(fuel, best)
print(best)
