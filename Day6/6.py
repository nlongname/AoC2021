with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    f.close

#test data
#data = ['3,4,3,1,2']

#ingest
fish = [data[0].count(str(i)) for i in range(9)]


#iterate
days = 256

for d in range(days):
    fish = fish[1:7]+[fish[7]+fish[0]]+[fish[8]]+[fish[0]]

print(sum(fish))
