import random
def CoinFlip():
    chance = 1
    HeadsStreak = 0
    StreakCounter = []
    TailsStreak = 0
    heads = 0
    tails = 0
    possibility = ["heads", "tails"]
    while chance <=100:
        flip = random.choice(possibility)
        chance +=1
        if(flip == "heads"):
            heads += 1
            StreakCounter.append("heads")
        else:
            tails += 1
            StreakCounter.append("tails")
    n = 0
    while n < len(StreakCounter):
        curVal = StreakCounter[n:(n+5)]
        if(len(curVal) == 5):
            if(curVal[0] == curVal[1] == curVal[2] == curVal [3]==  curVal[4] =="tails"):
                TailsStreak +=1
            elif(curVal[0] == curVal[1] == curVal[2] == curVal [3]==  curVal[4] =="heads"):
                HeadsStreak +=1
        n += 1
    print("Head Streak", HeadsStreak)
    print("Tails Streak",TailsStreak)
    print("No of Heads", heads)
    print("No of tails ", tails)
            

CoinFlip()