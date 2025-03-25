class Queue():
    def __init__(self):
        self.QueueArray = [ -1 for i in range(100)] #array upto 100 integer
        self.Headpointer = -1
        self.Tailpointer = 0
    
def  Enqueue(AQueue, TheData):
    if AQueue.Headpointer == -1:
        AQueue.QueueArray[AQueue.Tailpointer] = TheData
        AQueue.Headpointer = 0 
        AQueue.Tailpointer +=1
        return 1
    else:
        if AQueue.Tailpointer > 99:
            return -1
        else:
            AQueue.QueueArray[AQueue.Tailpointer] = TheData
            AQueue.Tailpointer = AQueue.Tailpointer +1
            return 1
        
def ReturnAllData(TheQueue):
    StrValue = ""
    
    for i in range(TheQueue.Headpointer, TheQueue.Tailpointer):
        value = TheQueue.QueueArray[i]
        if value != -1:
                    StrValue = (StrValue + " " + str(value) )

    return StrValue


def Dequeue(TheQueue):
    if TheQueue.Headpointer == TheQueue.Tailpointer or TheQueue.Headpointer == 100 or TheQueue.Headpointer == -1:
        return -1
    else:
        TheQueue.Headpointer += 1
        return TheQueue.QueueArray[TheQueue.Headpointer - 1]





if __name__ == "__main__":
    TheQueue = Queue()
    TheQueue.Headpointer = -1
    TheQueue.Tailpointer = 0

    
    flag = True
    i = 0
    while i < 10:
        try:
            usrData = int(input("Input an Integer Value of 0 or greater   -->    "))

            if usrData < 0:
                print("Error  - please enter a valid number\n")
            else:
                state = Enqueue(TheQueue, usrData)
                if state == -1:
                    print("The Queue is full:")
                else:
                    print(f"{usrData} has been added.")
                    i += 1
        except ValueError:
            print("Please enter an integer value")
    
    print(ReturnAllData(TheQueue))

    for i in range(2):
        state = Dequeue(TheQueue)
        if state == -1:
            print("The queue is empty.")
        else:
            print(f"{state} has been returned ")
        

    print(ReturnAllData(TheQueue))

