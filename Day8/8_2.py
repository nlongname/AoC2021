with open('input.txt', 'r+') as f:
    data = [line.strip('\n').split(' ') for line in f.readlines()]
    f.close

#put each code in alphabetical order, for simplicity
data = [[''.join(sorted(num)) for num in line] for line in data]

def decode(digits:list) -> dict:
    digits.sort(key=lambda x: len(x))
    one = digits[0]
    seven = digits[1]
    four = digits[2]
    eight = digits[-1]
    bd = [l for l in four if l not in one]
    five = [num for num in digits if len(num) == 5 and bd[0] in num and bd[1] in num][0]
    zero = [num for num in digits if len(num) == 6 and (bd[0] not in num or bd[1] not in num)][0]
    six = [num for num in digits if len(num) == 6 and (one[0] not in num or one[1] not in num)][0]
    nine = [num for num in digits if len(num) == 6 and num is not zero and num is not six][0]
    two = [num for num in digits if len(num) == 5 and (one[0] not in num or one[1] not in num) and num is not five][0]
    three = [num for num in digits if len(num)==5 and num is not two and num is not five][0]
    return {zero:'0', one:'1', two:'2', three:'3', four:'4', five:'5', six:'6', seven:'7', eight:'8', nine:'9'}

running_total = 0
for line in data:
    decoder = decode(line[:10])
    running_total += int(''.join([decoder[n] for n in line[-4:]]))
print(running_total)
