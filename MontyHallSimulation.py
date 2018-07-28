import random

def getSimNum():
    print('Enter the number of simulations to run, between 1 and 100000')
    while True:
        simNum = input()
        
        if not simNum.isdigit():
            print("Enter a number")
            continue
        if int(simNum) < 100001 and int(simNum) > 0:
            return int(simNum)
        print('Enter a number between 1 and 100000')

def playAgain():
    print('Do you want to run the simulation again? (yes or no)')
    return input().lower().startswith('y')

print('This simulation will play the Monty Hall game, switching\n'
      'every time. The computer will count how many times switching\n'
      'results in a win and display the resuts at the end.\n')

while True:
    switchWins = 0    
    simulations = getSimNum()
    
    for i in range(simulations):
        #set parameters
        doorNums = [1,2,3]
        blanks = ['_','_','_']
        winningDoor = random.randint(1,3)
    
        #computer makes firt move
        move = random.randint(1,3)
        blanks[move - 1] = 'X'
    
        #remove a losing door
        losingDoors = []
        for i in doorNums:
            if i != winningDoor and i != move:
                losingDoors.append(i)
    
        random.shuffle(losingDoors)
        doorToRemove = losingDoors[0]
    
        doorNums.remove(doorToRemove)
        del blanks[doorToRemove-1]
    
        #switch
        for i in range(len(blanks)):
            if blanks[i] == '_':
                blanks[i] = 'X'
            else:
                blanks[i] = '_'
        
        #determine winner
        winningDoorIndex = doorNums.index(winningDoor)
        if blanks[winningDoorIndex] == 'X':
            switchWins += 1
    
    print('Switch wins: %s (%s%%)' % (switchWins, round(switchWins / simulations * 100,1)))
    print('The theoretical probability of switching winning is 2/3.\n'
          'This is because the game removes an incorrect door, so\n'
          'if you are going to switch, all you need to do at the\n'
          'beginning is pick an incorrect door, because once you switch\n'
          'in round 2, there will only be a winning door to switch to.\n'
          'There are 2 wrong doors at the beginning, so you have a 2\n'
          'out of 3 chance of selecting a wrong door, which will then\n'
          'result in a win.')        
    if playAgain():
        True
    else:
        break

