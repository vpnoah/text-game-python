import random

random.seed()

health = 100
level = 1

enemyFile = open("enemies", "r")
weaponFile = open("weapons", "r")

enemyNames = []
weaponNames = []

while True:
    s = enemyFile.readline()
    if s == "":
        break
    s.strip()
    enemyNames.append(s)

while True:
    s = weaponFile.readline()
    if s == "":
        break
    s.strip()
    weaponNames.append(s)

while (health>0):

    enemyRand = random.randint(0,len(enemyNames)-1)
    weaponRand = random.randint(0,len(weaponNames)-1)


    eName = enemyNames[enemyRand].strip()
    wName = weaponNames[weaponRand].strip()
    enemyLevel = random.randint(level-5, level+7)
    if enemyLevel<1:
        enemyLevel = 1

    probability = 70
    dif = level - enemyLevel
    probability+= dif*5

    result = random.randint(0,100)

    print(eName + " appeared wielding a " + wName + " (Level " + 
        str(enemyLevel) + ")" + " \nProbality of victory is " + 
        str(probability) + "%")
    print("Fight (f) or Run (r)")

    while True:
        key = input()
        if key == "r":
            health -=5
            print("You ran")
            break
        if key == "f":

            if(result<probability):
                level +=1
                print("You won")
            else:
                health -=10
                print("You lost")

            break
        else:
            print("Please input f or r")

    

print("You made it to level " + str(level))
