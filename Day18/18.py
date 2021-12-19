from math import ceil
from functools import reduce
from ast import literal_eval

with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    f.close

def add(snail1:str,snail2:str) -> str:
    result = f'[{snail1},{snail2}]'
    return snailreduce(result)

def snailreduce(snail:str) -> str:
    old_snail = snail
    snail = explode(snail)
    if snail == old_snail:
        snail = split(snail)
        if snail == old_snail:
            return snail
    return snailreduce(snail)


def explode(snail:str) -> str:
    pointer = 0
    depth = 0
    while depth < 5 and pointer < len(snail):
        if snail[pointer] == '[':
            depth += 1
        elif snail[pointer] == ']':
            depth -= 1
        pointer += 1
    if depth == 5:
        current_nums = snail[pointer:pointer+snail[pointer:].index(']')].split(',')
        #print(current_nums)
        try:
            left_pointer = [i for i,x in enumerate(snail[:pointer]) if x.isnumeric()][-1]
            left_num = ''
            while snail[left_pointer].isnumeric():
                left_num = snail[left_pointer] + left_num
                left_pointer -= 1
            new_left = str(int(left_num)+int(current_nums[0]))
            snail = snail[:left_pointer+1]+new_left+snail[left_pointer+len(left_num)+1:]
            pointer = pointer - len(left_num) + len(new_left)
        except IndexError:
            pass
        try:
            right_pointer = [i+pointer+snail[pointer:].index(']') for i,x in enumerate(snail[pointer+snail[pointer:].index(']'):]) if x.isnumeric()][0]
            right_num = ''
            while snail[right_pointer].isnumeric():
                right_num += snail[right_pointer]
                right_pointer += 1
            new_right =str(int(right_num)+int(current_nums[1]))
            snail = snail[:right_pointer-len(right_num)]+new_right+snail[right_pointer:]
        except IndexError:
            pass
        current_nums = [int(n) for n in current_nums]
        snail = snail[:pointer-1]+'0'+snail[pointer+len(str(current_nums))-2:] #subtract one extra because str(current_nums) has an extra space
        #print('explode')
        #print(snail)
    return snail

def split(snail:str) -> str:
    try:
        index = [i for i in range(len(snail)) if snail[i].isnumeric() and snail[i+1].isnumeric()][0]
        snail = snail[:index]+f'[{int(snail[index:index+2])//2},{ceil(int(snail[index:index+2])/2)}]'+snail[index+2:]
    except IndexError:
        pass
    finally:
        #print('split')
        #print(snail)
        return snail

#use ast.literal_eval to turn into list-of-lists first, for recursion reasons
def magnitude(snail:str) -> int:
    return magnitude_helper(literal_eval(snail))

def magnitude_helper(snail:list or int) -> int:
    if type(snail) == int:
        return snail
    else:
        return 3*magnitude_helper(snail[0]) + 2*magnitude_helper(snail[1])

#part 1
result = data[0]
for d in data[1:]:
    result = add(result,d)
    #print(result)

print(magnitude(result))

#part 2
max_magnitude = 0
for x in data:
    for y in data:
        max_magnitude = max(max_magnitude,magnitude(add(x,y)))
        max_magnitude = max(max_magnitude,magnitude(add(y,x)))
print(max_magnitude)
