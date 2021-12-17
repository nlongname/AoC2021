# target area: x=150..171, y=-129..-70

left = 150
right = 171
bottom = -129
top = -70

count = 0

for xv in range(int((left*2)**.5),right+1):
    for yv in range(bottom,abs(bottom)+1):
        xvtemp = xv
        yvtemp = yv
        pos = (0,0)
        history = [pos]
        while pos[0] <= right and pos[1] >= bottom:
            pos = (pos[0]+xvtemp, pos[1]+yvtemp)
            if pos[0] in range(left,right+1) and pos[1] in range(bottom,top+1):
                count += 1
                break
            if xvtemp > 0:
                xvtemp -= 1
            yvtemp -= 1
print(count)
