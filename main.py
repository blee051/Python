# This is Brandon's TikTakToe game:
# Sudo: Create 3x3 Matrix list
# Each element of the matrix have 3 representations: Blank, X, and O
# Print Game
# Player 1 will select a coordinates Top left, Middle middle, bottom right, etc
# See if coordinates is available
# If so, update Matrix. Elif Error message and tell player to choose again
# Check for three in a row
# -Use loop to check every possible three in-a-row
# --If found, print win screen along with player number, elif Print TikTakTow with current matrix
# Next player

def printTikTakTow(m):
    i=0
    while i<3:
        print(m[i][0]+"|"+m[i][1]+"|"+m[i][2])
        if i<2:
            print("-----")
        i+=1
    return


def playerCommand(p, mmap, g, l):
    print("Coordinates: Top Left, Top Middle, Top Right")
    print("Middle Left, Middle Middle, Middle Right")
    print("Bottom Left, Bottom Middle, Bottom Right")
    print("Player",p,": ")
    coordinate = input("Select your move:  ")
    gameRow = 0
    gameCol = 0
    correctInput = False

    # Checking for correct input
    for element in g:
        for e in element:
            if e == coordinate:
                if mmap[gameRow][gameCol] != ' ':
                    print("Position Already Taken")
                else:
                    mmap[gameRow][gameCol] = playerLetter
                    correctInput=True
                    break
            gameCol+=1
        gameCol=0
        gameRow+=1
    if correctInput == False:
        print("Incorrect Input! Try Again")
        mmap=playerCommand(p,mmap,g,l)
    return mmap


def checkConnectThree(m, lletter, pplayer):
    otherLetter = 'X'
    if lletter == 'X':
        otherLetter = 'O' # I forgot why i did this
    rowMatchAmmount = 0
    collumMatchAmmount = 0
    # We are checking the rows and collums for connect 3's by counting the letter of the current player
    i=0
    r=0
    while r<3:
        while i<3:
            if m[i][r] == lletter:
                rowMatchAmmount += 1 # row count
            if m[r][i] == lletter:
                collumMatchAmmount += 1 # collum count
            i+=1

        if rowMatchAmmount == 3:
            print("Player ",pplayer," WINS!")  # WIN
            return True
        if collumMatchAmmount == 3:
            print("Player ",pplayer,"WINS!")  # Insert Win here
            return True

        rowMatchAmmount = 0
        collumMatchAmmount = 0
        i=0
        r+=1
    # We are checking the diagnols this time
    diagnalOneMatch = 0
    diagnalTwoMatch = 0
    y=0
    z=2
    while y<3:
        if m[y][y] == lletter:
            diagnalOneMatch += 1  # Diagnol count
        if m[y][z] == lletter:
            diagnalTwoMatch += 1 # Other diagnol count
        y+=1
        z-=1

    if diagnalOneMatch == 3:
        print("Player ",pplayer,"WINS!")  # Win Prompt
        return True
    if diagnalTwoMatch == 3:
        print("Player ",pplayer,"WINS!")  # Other win Promt
        return True
    return False

#Setting up the matrix, both the virtual game and its positioning
m = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
gameMap = [["Top Left", "Top Middle", "Top Right"], ["Middle Left", "Middle Middle", "Middle Right"],
           ["Bottom Left", "Bottom Middle", "Bottom Right"]]

player = 1
playerLetter = 'X'
gameOver = False
while gameOver == False:
    printTikTakTow(m) #Print virtual game
    m = playerCommand(player, m, gameMap, playerLetter) # update map
    gameOver = checkConnectThree(m, playerLetter, player) # check victory condition
    if player == 1:  # swap player and letter
        player = 2
        playerLetter = 'O'
    else:
        player = 1
        playerLetter = 'X'


