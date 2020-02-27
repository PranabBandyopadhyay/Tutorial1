from printBoardrun import draw
from EX26 import play


sample = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

print("                TICK TAK TOE          ")
print("please follow below sample for your input")
draw(3,3,sample)

gameboard = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

def position(a):
    if a == 1:
        return [0,0]
    elif a == 2:
        return [0,1]
    elif a == 3:
        return [0,2]
    elif a == 4:
        return [1,0]
    elif a == 5:
        return [1,1]
    elif a == 6:
        return [1,2]
    elif a == 7:
        return [2,0]
    elif a == 8:
        return [2,1]
    elif a == 9:
        return [2,2]
winner = None
game_counter=0
played = []
while winner == None and game_counter < 9:
    player1 = int(input("Player 1, please input you choice"))
    if player1 in range(1,10) and player1 not in played:
        played.append(player1)
        lat,long = position(player1)
        gameboard[lat][long] = "X"
        draw(3, 3, gameboard)
    else:
        print("Illegal Entry. Penalty !!!")
    winner = play(gameboard)
    game_counter += 1
    if winner == None and  game_counter < 9:
        player2 = int(input("Player 2, please input you choice"))
        if player2 in range(1,10) and player2 not in played:
            played.append(player2)
            lat, long = position(player2)
            gameboard[lat][long] = "O"
            draw(3, 3 ,gameboard)
        else:
            print("Illegal Entry. Penalty !!!")
        winner = play(gameboard)
    game_counter += 1

if winner == "X":
    print("Winner is Player1")
elif winner == "O":
    print("Winner is Player2")
elif winner == None:
    print("Its a Draw")