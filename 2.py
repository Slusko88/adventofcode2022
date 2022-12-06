strategyguide = []


with open("in-2.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        splits = line.split(' ')
        strategyguide.append((splits[0], splits[1]))

ROCK        = 0
PAPER       = 1
SCISSORS    = 2
LOSS = 3
DRAW = 4
WIN = 5

OPPONENT    = ['A','B','C']
ME          = ['X','Y','Z']
POINTS = [1,2,3,0,3,6]

DESIRED_LOSS = 0
DESIRED_DRAW = 1
DESIRED_WIN  = 2
def play(opponent, me):
    result = None
    if opponent == ROCK:
        if me == PAPER:
            result = POINTS[WIN]
        elif me == ROCK:
            result = POINTS[DRAW]
        elif me == SCISSORS:
            result = POINTS[LOSS]
        else:
            result = None
    elif opponent == PAPER:
        if me == PAPER:
            result = POINTS[DRAW]
        elif me == ROCK:
            result = POINTS[LOSS]
        elif me == SCISSORS:
            result = POINTS[WIN]
        else:
            result = None
    elif opponent == SCISSORS:
        if me == PAPER:
            result = POINTS[LOSS]
        elif me == ROCK:
            result = POINTS[WIN]
        elif me == SCISSORS:
            result = POINTS[DRAW]
        else:
            result = None

    if result != None:
        result += POINTS[me]

    return result

def applyStrategy(desiredResult, opponentHand):
    myHand = None
    if desiredResult == DESIRED_DRAW:
        myHand = opponentHand
    elif desiredResult == DESIRED_LOSS:
        if opponentHand == ROCK:
            myHand = SCISSORS
        if opponentHand == PAPER:
            myHand = ROCK
        if opponentHand == SCISSORS:
            myHand = PAPER
    elif desiredResult == DESIRED_WIN:
        if opponentHand == ROCK:
            myHand = PAPER
        if opponentHand == PAPER:
            myHand = SCISSORS
        if opponentHand == SCISSORS:
            myHand = ROCK

    return myHand

scores = []
totalScore= 0
for case in strategyguide:
    opponentHand = None
    myHand = None
    for i in range(0,len(OPPONENT)):
        if OPPONENT[i] == case[0]:
            opponentHand = i
            break
    for i in range(0,len(ME)):
        if ME[i] == case[1]:
            myHand = i
            break
    myHand = applyStrategy(myHand, opponentHand)
    score = play(opponentHand, myHand)

    scores.append((case, score))
    totalScore += score

#print(scores)
print('Total Score is: ', str(totalScore))

