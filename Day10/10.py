from functools import reduce

with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    f.close

lefts = {'(', '[', '{', '<'}
opp = {'(':')',')':'(','[':']',']':'[','{':'}','}':'{','<':'>','>':'<'}

def corrupt_score(line:str) -> int:
    score = {')':3,']':57,'}':1197,'>':25137}
    queue = []
    for c in line:
        if c in lefts:
            queue.append(c)
        else:
            if queue[-1] == opp[c]:
                queue = queue[:-1]
            else:
                return score[c]
    return 0

syntax_score = sum([corrupt_score(line) for line in data])
print(syntax_score)

def completion_score(line:str) -> int:
    score = {'(':1,'[':2,'{':3,'<':4}
    queue = []
    for c in line:
        if c in lefts:
            queue.append(c)
        else:
            if queue[-1] == opp[c]:
                queue = queue[:-1]
            else:
                return 0
    scores = [score[c] for c in reversed(queue)]
    return reduce(lambda x,y: x*5+y,scores)

completion_scores = [completion_score(line) for line in data]
completion_scores = [score for score in completion_scores if score != 0]
completion_scores.sort()
print(completion_scores[len(completion_scores)//2])
