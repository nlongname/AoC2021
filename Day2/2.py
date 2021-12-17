with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    f.close
forwards = [int(d.strip('forward')) for d in data if d.startswith('forward')]
downs = [int(d.strip('down')) for d in data if d.startswith('down')]
ups = [int(d.strip('up')) for d in data if d.startswith('up')]
horiz = sum(forwards)
depth = sum(downs)-sum(ups)
print(f"final position: horizontal {horiz}, depth {depth}")
print(f"answer: {horiz*depth}")


depth=0
horiz=0
aim=0
for d in data:
    if d.startswith('forward'):
        num = int(d.strip('forward'))
        horiz += num
        depth += num*aim
    elif d.startswith('up'):
        num = int(d.strip('up'))
        aim -= num
    elif d.startswith('down'):
        num = int(d.strip('down'))
        aim += num
print(f"true final position: horizontal {horiz}, depth {depth}")
print(f"true answer: {horiz*depth}")
