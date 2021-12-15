with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    f.close

#test data
#data = ['NNCB', '', 'CH -> B', 'HH -> N', 'CB -> H', 'NH -> C', 'HB -> C', 'HC -> B', 'HN -> C', 'NN -> C', 'BH -> H', 'NC -> B', 'NB -> B', 'BN -> B', 'BB -> N', 'BC -> B', 'CC -> N', 'CN -> C']

polymer = data[0]

#setup
ruledict = {}
for rule in data[2:]:
    ruledict[rule[:2]] = rule[-1]
paircounts = {pair:int(pair in polymer) for pair in ruledict}

def apply(rules:dict, oldcounts:dict) -> dict: #updates the counts for each pair of letters and returns it
    newcounts = {pair:0 for pair in oldcounts}
    for p in oldcounts:
        newcounts[p[0]+rules[p]] += oldcounts[p]
        newcounts[rules[p]+p[1]] += oldcounts[p]
    return newcounts

#apply rules 10 or 40 times
for i in range(40):
    paircounts = apply(ruledict, paircounts)

#convert to letter counts
lettercounts = {}
# this process double-counts all letters besides the first and last
# but the first and last letters are the same as they were when we started
for pair in paircounts:
    if pair[0] in lettercounts:
        lettercounts[pair[0]] += paircounts[pair]
    else:
        lettercounts[pair[0]] = paircounts[pair]
    if pair[1] in lettercounts:
        lettercounts[pair[1]] += paircounts[pair]
    else:
        lettercounts[pair[1]] = paircounts[pair]
lettercounts[polymer[0]] += 1 #so we double-count the first and last letters
lettercounts[polymer[-1]] += 1
lettercounts = {l:lettercounts[l]//2 for l in lettercounts} #then divide by 2
print(max(lettercounts.values()) - min(lettercounts.values()))
