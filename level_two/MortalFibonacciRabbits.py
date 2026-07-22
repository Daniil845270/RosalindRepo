overallGenerations, deathGeneration = int(input()), int(input())

born = 1
mature = 0
bornByGenerations = [1]


for n in range(deathGeneration - 1):
    temp = born
    born = mature
    bornByGenerations.append(born)
    mature += temp

for n in range(overallGenerations - deathGeneration):
    temp = born
    born = mature
    bornByGenerations.append(born)
    mature += temp
    died = bornByGenerations.pop(0)
    mature -= died

print(born + mature)