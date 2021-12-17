# target area: x=150..171, y=-129..-70
# x-velocity is tied to triangular numbers, find the limits based on that
# (higher x-velocities are possible but would have to minimize y-velocity)
# arc always hits the same heights on the way down as up
# so y-velocity can't be higher than abs(bottom of target area)

left = 150
right = 171
bottom = -129
top = -70

max_height = 0 #at least in our case this isn't high enough, 0 y-velocity will miss low
xv_max = 0
yv_max = 0

for xv in range(int((left*2)**.5),int((right*2)**.5)+1):
    for yv in range(0,abs(bottom)+1):
        xvtemp = xv
        yvtemp = yv
        pos = (0,0)
        history = [pos]
        while pos[0] <= right and pos[1] >= bottom:
            pos = (pos[0]+xvtemp, pos[1]+yvtemp)
            history.append(pos)
            if xvtemp > 0:
                xvtemp -= 1
            yvtemp -= 1
        if history[-2][0] in range(left,right+1) and history[-2][1] in range(bottom,top+1):
            height = max(history,key=lambda p: p[1])[1]
            if height > max_height:
                max_height = height
                xv_max, yv_max = xv, yv
print(xv_max, yv_max, max_height)
