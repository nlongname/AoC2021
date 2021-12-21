#Player 1 starting position: 2
#Player 2 starting position: 1

#for the sake of convenience, I'm thinking of them as player 0 and player 1

scores = [0,0]
positions = [2,1]
turn = 0
next_die = 1
while max(scores) < 1000:
    positions[turn] = ((positions[turn] + next_die%100 + (next_die+1)%100 + (next_die+2)%100)-1)%10 + 1 #-1 then mod then +1 changes it from 0-9 to 1-10
    next_die += 3
    scores[turn] += positions[turn]
    turn = 1-turn

print(min(scores)*(next_die-1))
