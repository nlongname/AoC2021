with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    f.close

#ingest data to the form ['on'/'off', (x1,x2), (y1,y2), (z1,z2)]
new_data = []
for l in data:
    direction = 'on' if l.startswith('on') else 'off'
    entry = [direction]
    p1 = l.index('=')
    p2 = l.index('..')
    for i in range(2):
        temp = int(l[p1+1:p2])
        p1 = l.index('=',p2)
        c = (temp, int(l[p2+2:p1-2]))
        entry.append(c)
        p2 = l.index('..',p1)
    c = (int(l[p1+1:p2]), int(l[p2+2:]))
    entry.append(c)
    #for part 1
    #if max([max(abs(c[0]),abs(c[1])) for c in entry[1:]]) <= 50:
    new_data.append(entry)

#core concept: we're going to make all instructions meaningful, so none
#go from off->off or on->on. 'off' is the default, since that's where we start
#so all off instructions will be replaced entirely by their intersections
#with previous instructions.
#on instructions need to be left in place, but we'll "fix" the intersections
#by inserting deletions of the intersection beforehand. similarly off instr's
#similarly, when we have off->off we'll insert an on so it's off->-on->off
#This way any instruction can be interpreted as its "base" number of cubes
#added (0 for off, x*y*z for on) minus any overlap with an 'on' instruction
#(they're already on) plus any overlap with an 'off' instruction

total = 0
pointer = 0
while pointer < len(new_data):
    instr = new_data[pointer]
    direction, x, y, z = instr
    if direction == 'on':
        instr_total = (x[1]-x[0]+1)*(y[1]-y[0]+1)*(z[1]-z[0]+1) #+1 b/c they're inclusive
    else:
        instr_total = 0
    overlap_list = []
    for i in new_data[:pointer]:
        sign = -1 if i[0] == 'on' else 1
        overlap = [(max(i[1][0],x[0]),min(i[1][1],x[1])), (max(i[2][0],y[0]),min(i[2][1],y[1])), (max(i[3][0],z[0]),min(i[3][1],z[1]))]
        if overlap[0][1]>=overlap[0][0] and overlap[1][1]>=overlap[1][0] and overlap[2][1]>=overlap[2][0]:
            instr_total += sign*(overlap[0][1]-overlap[0][0]+1)*(overlap[1][1]-overlap[1][0]+1)*(overlap[2][1]-overlap[2][0]+1)
            overlap_list.append(['on' if i[0]=='off' else 'off']+overlap)
            #it seems weird that off+off -> on, but it works out on the whole
            #if a block has been turned on then off already and we turn it off
            #this replaces our off instr. with an off and an on (i.e. nothing
            #happens, as expected). This only works because we know all prev.
            #instructions are meaningful and without overlap
    total += instr_total
    #print(total)
    if direction == 'off':
        new_data = new_data[:pointer] + overlap_list + new_data[pointer+1:]
        pointer += len(overlap_list)
    else:
        new_data = new_data[:pointer] + overlap_list + new_data[pointer:]
        pointer += len(overlap_list) + 1
print(total)
