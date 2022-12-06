



elfsCalories = []

with open("in-1.txt", "r") as f:
    lines = f.readlines()
    calorieSum = 0
    for line in lines:
        if line == '\n' or 0 == len(line):
            elfsCalories.append(calorieSum)
            calorieSum = 0
        else:
            calorieSum += int(line)


print('Elf with max calories: ' + str(max(elfsCalories)))

elfsCalories.sort(reverse=True)
top3caloriesum = 0
for i in range(0,3):
    top3caloriesum += elfsCalories[i]
print('Top3 calorie sum:' + str(top3caloriesum))