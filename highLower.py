import os
import random

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

def randomData(tempData):
    while(True):
            a = random.randint(0,len(tempData)-1)
            b = random.randint(0,len(tempData)-1)
            if(a!=b):
                return(a,b)

def validateUserGuess():
    while(True):
            userGuess = input("Who has more followers? Type 'A' or 'B': ").lower()
            if(userGuess=='a' or userGuess=='b'):
                break
            else:
                print("select 'A' or 'B' : ")
    return userGuess

def checkCondition(tempData,userGuess,a,b):
    if(tempData[a]['followers']>tempData[b]['followers'] and userGuess=='a'):
            userScore += 1
            tempData.pop(a)
            return userScore

    elif(tempData[a]['followers']>tempData[b]['followers'] and userGuess=='b'):
        print("you lost...")
        return -1

    elif(tempData[a]['followers']<tempData[b]['followers'] and userGuess=='b'):
        userScore += 1
        tempData.pop(b)
        return userScore

    elif(tempData[a]['followers']<tempData[b]['followers'] and userGuess=='a'):
        print("you lost...")
        return -1

def play():
    playAgain='y'
    while(playAgain.lower()=='y'):
        tempData = list(data)
        userScore=0
        while(len(tempData)-1):
            a,b=randomData(tempData)
            print(f"Compare A: {tempData[a]['name']},{tempData[a]['profession']},from {tempData[a]['location']} ")
            print("..........vs.........")
            print(f"Against B: {tempData[b]['name']},{tempData[b]['profession']},from {tempData[b]['location']} ")
            userGuess = validateUserGuess()
            userScore = checkCondition(tempData,userGuess,a,b)
            os.system('cls')
            print(f"your current score is :{userScore}")
            if userScore==-1:
                break
    print(f"your final score is :{userScore}")
    playAgain = input("Do you want to play again (y/n): ")

    print("Game Over...")

play()