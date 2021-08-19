# ANoTheR TIKTAKTTOE GAME BUT WITH CLASS
# SUDO: I WILL USE CLASS TO DEFINE THE PLAYER
# PLAYER.NUMBER, PLAYER.CHARACTER,
# I WILL USE CLASS TO DEFINE TICTAKTOE
# TICTAKTOE.GAME_MAP, TICTAKTOE.GAME_LOCATION
# FROM THERE I WILL MAKE THE GAME AS I DID ON THE PREVIOUS VERSION

class Player:
    def __init__(self, number, character):
        self.number = number
        self.character = character

class TikTakToe:
    def __init__(self):
        self.game_map = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.game_location = [["Top Left", "Top Middle", "Top Right"], ["Middle Left", "Middle Middle", "Middle Right"],
           ["Bottom Left", "Bottom Middle", "Bottom Right"]]

def print_map(m):
    i=0
    while i<3:
        print(m[i][0]+"|"+m[i][1]+"|"+m[i][2])
        if i<2:
            print("-----")
        i+=1
    return

def print_instructions():
    print("These are the coordinates from which you can choose:")
    print("   Top Left |   Top Middle  | Top Right")
    print("Middle Left | Middle Middle | Middle Right")
    print("Bottom Left | Bottom Middle | Bottom Right")
    print("Please type in correctly; they are case sensitive")
    return

def player_command(p, mmap, g, l):
    print("Player",p,": ")
    coordinate = input("Select your move:  ")
    gameRow = 0
    gameCol = 0
    correctInput = False

    for element in g:
        for e in element:
            if e == coordinate:
                if mmap[gameRow][gameCol] != ' ':
                    print("Position Already Taken")
                else:
                    mmap[gameRow][gameCol] = l
                    correctInput=True
                    break
            gameCol+=1
        gameCol=0
        gameRow+=1
    if correctInput == False:
        print("Incorrect Input! Try Again")
        mmap=player_command(p,mmap,g,l)
    return mmap

def check_connect_three(m, lletter, pplayer):
    rowMatchAmmount = 0
    collumMatchAmmount = 0

    i=0
    r=0
    while r<3:
        while i<3:
            if m[i][r] == lletter:
                rowMatchAmmount += 1
            if m[r][i] == lletter:
                collumMatchAmmount += 1
            i+=1

        if rowMatchAmmount == 3:
            print("Player ",pplayer," WINS!")
            print_map(m)
            return True
        if collumMatchAmmount == 3:
            print("Player ",pplayer,"WINS!")
            print_map(m)
            return True

        rowMatchAmmount = 0
        collumMatchAmmount = 0
        i=0
        r+=1

    diagnalOneMatch = 0
    diagnalTwoMatch = 0
    y=0
    z=2
    while y<3:
        if m[y][y] == lletter:
            diagnalOneMatch += 1
        if m[y][z] == lletter:
            diagnalTwoMatch += 1
        y+=1
        z-=1

    if diagnalOneMatch == 3:
        print("Player ",pplayer,"WINS!")
        print_map(m)
        return True
    if diagnalTwoMatch == 3:
        print("Player ",pplayer,"WINS!")
        print_map(m)
        return True
    return False

def change_turn(p, p1, p2):
    if p == 1:
        return p2
    else:
        return p1

# main()
ttt1 = TikTakToe()
player1 = Player(1, "X")
player2 = Player(2, "O")
current_player = Player(player1.number, player1.character)
gameOver = False
print_instructions()
while gameOver == False:
    print_map(ttt1.game_map)
    ttt1.game_map = player_command(current_player.number, ttt1.game_map, ttt1.game_location, current_player.character)
    gameOver = check_connect_three(ttt1.game_map, current_player.character, current_player.number)
    current_player = change_turn(current_player.number, player1, player2)
