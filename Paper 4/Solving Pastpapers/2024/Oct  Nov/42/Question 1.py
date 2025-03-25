#Declaring Class EventItem to store about the events
class EventItem():
    def __init__(self, pEventName, pType, pDifficulty):
        self.__EventName = pEventName  # stores the name of the event
        self.__EventType = pType #stores the type of event, either: jump, swim, run or drive
        self.__Difficulty = pDifficulty #difficulty of the event from 1 (easiest) to 5 (hardest)


    def Getname(self):
        return self.__EventName
    
    def GetDifficulty(self):
        return self.__Difficulty
    
    def GetEventType(self):
        return self.__EventType
    
#class Character stores data about the characters in the game.



class Character():
    def __init__(self, pcharactername, pJump, pSwin, pRun, pDrive):
        self.__CharacterName = pcharactername
        self.__Jump = pJump
        self.__Swim = pSwin
        self.__run = pRun
        self.__Drive = pDrive

    def GetName(self):
        return self.__CharacterName
    
    def CalculateScore(self, Type, Dif):
        if Type == "jump":
            chance = self.__Jump
        elif Type == "swim":
            chance = self.__Swim
        elif Type == "run":
            chance = self.__run
        elif Type == "drive":
            chance = self.__Drive
        
        Difference = Dif - chance

        if chance >= Dif:
            return 100
        elif Difference == 1:
            return 80
        elif Difference == 2:
            return 60
        elif Difference == 3:
            return 40
        elif Difference == 4:
            return 20

        

            

Group = [] #type Event, 5 spaces

Group.append(EventItem("Bridge", "jump", 3))
Group.append(EventItem("Water wade", "swim", 4))
Group.append(EventItem("100 mile run", "run", 5))
Group.append(EventItem("Gridlock", "drive", 2))
Group.append(EventItem("Wall on wall", "jump", 4))



Tarz = Character("Tarz", 5, 3, 5, 1)
Geni = Character("Geni", 2, 2, 3, 4)
Scorep1 = 0
Scorep2  =0 
for i in range(0, 4):
    EventName = Group[i].Getname()
    EventType = Group[i].GetEventType()
    EventDif = Group[i].GetDifficulty()
    p1 = Tarz
    p2 = Geni


    ChanceP1 = p1.CalculateScore(EventType, EventDif)
    ChanceP2 = p2.CalculateScore(EventType, EventDif)

    if ChanceP1 > ChanceP2:
        Scorep1 += 1
        print(f"{Tarz.GetName()} you have won {EventName} and your score now is {Scorep1}")
    elif ChanceP2 >ChanceP1:
        Scorep2 += 1
        print(f"{Geni.GetName()} you have won {EventName} and your score now is {Scorep2}")
    elif ChanceP1 == ChanceP2:
        print(f"It was a draw between {Tarz.GetName()} and {Geni.GetName()} at {EventName}")
    
if Scorep1 > Scorep2:
    print(f"Tarz has won this group with teh score of {Scorep1}")
elif Scorep2 > Scorep1:
    print(f"Geni has won this group with teh score of {Scorep2}")
elif Scorep2 == Scorep1:
    print("both the players had the same score so it was a draw")
      