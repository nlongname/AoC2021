with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    f.close

data = [line.split('-') for line in data]

#set up connection map
connections = {}
for l in data:
    if l[0] not in connections:
        connections[l[0]] = [l[1]]
    else:
        if l[1] not in connections[l[0]]:
            connections[l[0]].append(l[1])
    if l[1] not in connections:
        connections[l[1]] = [l[0]]
    else:
        if l[0] not in connections[l[1]]:
            connections[l[1]].append(l[0])

leads = [(['start'],['start'])] 
done = 0
while leads != []:
    current_path, forbidden = leads[0]
    candidates = [c for c in connections[current_path[-1]] if c not in forbidden]
    if 'end' in candidates:
        done += 1
        #print(done, current_path, forbidden)
        candidates.remove('end')
    for c in candidates:
        if c.islower():
            #this is awkward, but it puts the longer paths first so they'll pop sooner
            leads = [(current_path+[c],forbidden+[c])]+leads
        else:
            leads = [(current_path+[c],forbidden)]+leads
    leads.remove((current_path, forbidden))
print(done)
