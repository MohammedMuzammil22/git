import os
import random
print("Higher-Lower")

data = [
    {
        "name":"Muzammil",
        "followers":500,
        "profession":"coder",
        "location":"India"
    },
    {
        "name":"Abu",
        "followers":100,
        "profession":"web",
        "location":"us"
    },
    {
        "name":"aasim",
        "followers":300,
        "profession":"ui",
        "location":"uk",
    },
    {
        "name":"arshad",
        "followers":503,
        "profession":"cloud",
        "location":"china",
    },
    {
        "name":"fahim",
        "followers":23,
        "profession":"tester",
        "location":"canada",
    }
]

playAgain='y'
while(playAgain.lower()=='y'):
    tempData = list(data)
    userScore=0
    while(len(tempData)-1):
        while(True):
            a = random.randint(0,len(tempData)-1)
            b = random.randint(0,len(tempData)-1)
            if(a!=b):
                break
        # for i in range(len(tempData)):
        #     print(tempData[i]['name'])
        print(f"Compare A: {tempData[a]['name']},{tempData[a]['profession']},from {tempData[a]['location']} ")
        print("..........vs.........")
        print(f"Against B: {tempData[b]['name']},{tempData[b]['profession']},from {tempData[b]['location']} ")
        while(True):
            userGuess = input("Who has more followers? Type 'A' or 'B': ").lower()
            if(userGuess=='a' or userGuess=='b'):
                break
            else:
                print("select 'A' or 'B' : ")
        if(tempData[a]['followers']>tempData[b]['followers'] and userGuess=='a'):
            userScore += 1
            tempData.pop(a)

        elif(tempData[a]['followers']>tempData[b]['followers'] and userGuess=='b'):
            print("you lost...")
            break

        elif(tempData[a]['followers']<tempData[b]['followers'] and userGuess=='b'):
            userScore += 1
            tempData.pop(b)

        elif(tempData[a]['followers']<tempData[b]['followers'] and userGuess=='a'):
            print("you lost...")
            break

        os.system('cls')
        print(f"your current score is :{userScore}")
    print(f"your final score is :{userScore}")
    playAgain = input("Do you want to play again (y/n): ")

print("Game Over...")




