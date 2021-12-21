#Player 1 starting position: 2
#Player 2 starting position: 1

#for the sake of convenience, I'm thinking of them as player 0 and player 1
#(at least until the last step)

in_progress = {(2,1,0,0,0):1} #(position0, position1, score0, score1,turn):number of universes
one_wins = 0
two_wins = 0

while in_progress != {}:
    current = list(in_progress.keys())[0]
    count = in_progress[current]
    for i in range(1,4):
        for j in range(1,4):
            for k in range(1,4):
                positions = list(current[0:2])
                scores = list(current[2:4])
                turn = current[4]
                positions[turn] = (positions[turn] + i + j + k - 1)%10 + 1 #-1 then mod then +1 changes it from 0-9 to 1-10
                scores[turn] += positions[turn]
                turn = 1-turn
                new_state = (positions[0],positions[1],scores[0],scores[1],turn)
                if max(scores) >= 21:
                    if scores[0] > scores[1]:
                        one_wins += count
                    else:
                        two_wins += count
                elif new_state in in_progress:
                    in_progress[new_state] += count
                else:
                    in_progress[new_state] = count
    del in_progress[current]

#one_wins = sum([done[u] for u in done if u[2]>u[3]])
#two_wins = sum([done[u] for u in done if u[3]>u[2]])
if one_wins > two_wins:
    print(f"one won {one_wins} times")
else:
    print(f"two won {two_wins} times")
