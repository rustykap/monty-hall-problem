import random

doorNums = [1,2,3]
blanks = ['_','_','_']
winningDoor = random.randint(1,3)

def drawBoard():
    for i in doorNums:
        print(i, end=' ')
    print()
    for i in blanks:
        print(i, end=' ')
    print()
    print()

def getMove():
    move = ''
    while move not in ['1','2','3']:
        print('Select a door: 1, 2 or 3')
        move = input()
    return int(move)


def makeMove(move):
    blanks[move - 1] = 'X'

def removeLosingDoor(move):
    losingDoors=[]
    for i in doorNums:
        if i != winningDoor and i != move:
            losingDoors.append(i)

    random.shuffle(losingDoors)
    doorToRemove = losingDoors[0]

    doorNums.remove(doorToRemove)
    del blanks[doorToRemove-1]
    

def switchChoice():
    choice = ''
    while choice not in 'yes y no n'.split():
        print ('Do you want to switch? Yes or no?')
        choice = input().lower()
        print()
    if choice == 'y' or choice == 'yes':
        for i in range(len(blanks)):
            if blanks[i] == '_':
                blanks[i] = 'X'
            else:
                blanks[i] = '_'
                
    return blanks

def reveal():
    winningDoorIndex = doorNums.index(winningDoor)
    if blanks[winningDoorIndex] == 'X':
        print('YOU WIN!!!!!!!!!!')
    else:
        print('YOU LOSE :(')
    blanks[winningDoorIndex] = 'O'

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

while True:        
    print('Welcome to the famous Monty Hall game. There is a prize\n'
          'hidden behind one of three doors. You will have to pick\n'
          'which door you think the prize is behind. After you have picked\n'
          'a door, we will remove a door that does not contain the prize.\n' 
          'You will then be given the option to switch your selection\n'
          'or stick with it.\n\n'
          'Lets play\n')
    input('Press ENTER when ready\n')
    drawBoard()
    firstMove = getMove()
    makeMove(firstMove)
    print()
    print('The X marks your door selection below')
    print()
    drawBoard()
    removeLosingDoor(firstMove)
    print('We will now remove a losing door')
    print()
    input('Press ENTER when ready')
    print()
    drawBoard()

    switchChoice()
    drawBoard()

    reveal()
    drawBoard()
    print('The theoretical probability of switching winning is 2/3.\n'
          'This is because the game removes an incorrect door, so\n'
          'if you are going to switch, all you need to do at the\n'
          'beginning is pick an incorrect door, because once you switch\n'
          'in round 2, there will only be a winning door to switch to.\n'
          'There are 2 wrong doors at the beginning, so you have a 2\n'
          'out of 3 chance of selecting a wrong door, which will then\n'
          'result in a win.')
    if playAgain():
        doorNums = [1,2,3]
        blanks = ['_','_','_']
        winningDoor = random.randint(1,3)
    else:
        break
