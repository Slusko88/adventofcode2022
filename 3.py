



rucksacks = []
with open("in-3.txt",'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip('\n')
        size = len(line)
        com1 = line[0:size//2]
        com2 = line[size//2:size]
        if(len(com1) != len(com2)):
            print('Compartment size not equal!')
        rucksacks.append((com1,com2))

def findMixedItems(rucksack):
    com1 = rucksack[0]
    com2 = rucksack[1]
    mixed_items = []
    for item in com1:
        if item in com2:
            mixed_items.append(item)

    return mixed_items

def getpriority(item):
    prio = None
    if item.islower():
        prio = ord(item) - ord('a') +1
    else:
        prio = ord(item) - ord('A') + 27

    return prio

itemsPrioSum = 0
for rucksack in rucksacks:
    mixeditems = findMixedItems(rucksack)
    mixeditems = list(dict.fromkeys(mixeditems)) # remove duplicates
    for item in mixeditems:
        itemsPrioSum += getpriority(item)

print(itemsPrioSum)

groupPrioSum = 0
for idx in range(0,len(rucksacks),3):
    group = rucksacks[idx: idx+3]
    commonitems = []
    for rucksack in group:
        commonitems.append(rucksack[0] + rucksack[1])
    commonitem = set(commonitems[0]).intersection(commonitems[1])
    commonitem = set(commonitem).intersection(commonitems[2])
    groupPrioSum += getpriority(str(commonitem.pop()))

print('Group prio: ' + str(groupPrioSum))