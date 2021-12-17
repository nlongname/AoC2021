from functools import reduce

with open('input.txt', 'r+') as f:
    data = [line.strip('\n') for line in f.readlines()]
    f.close
numbers = [int(x) for x in data[0].split(',')]

boards = [[data[j].split(' ') for j in range(i,i+5)]for i in range(2,len(data),6)]

boards = [[[int(x) for x in r if x != ''] for r in b] for b in boards]
#currently has horizontal rows only, let's add columns
size = len(boards[0][0])
for b_i in range(len(boards)):
    for c in range(size):
        boards[b_i].append([r[c] for r in boards[b_i][:size]])

def winner_check(board_list:list) -> list: #check if there's a winner and return it; if not the empty list
    for b in board_list:
        if [] in b:
            return b
    return []

def play_to_win(nums:int, board_list:list) -> int:
    winner = []
    while winner == []:
        current = nums.pop(0)
        board_list = [[[int(x) for x in r if x != current] for r in b] for b in board_list]
        winner = winner_check(board_list)
    score = current * sum([sum(r) for r in winner])//2 #divide by 2 because we're double-counting w/ horiz and vert. lists
    return score

#print(play_to_win(numbers, boards))

def play_to_lose(nums:int, board_list:list) -> int:
    winner = []
    while len(board_list) > 1:
        current = nums.pop(0)
        board_list = [[[int(x) for x in r if x != current] for r in b] for b in board_list]
        winner = winner_check(board_list)
        while winner != []:
            board_list.remove(winner)
            winner = winner_check(board_list) #since this fxn only finds one at a time
    #now we've found our last winner, but we need to play until it wins
    return play_to_win(nums, board_list)
print(play_to_lose(numbers, boards))
