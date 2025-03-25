
def Initialise(): 
    global DataStored 
    global NumberItems 
    Valid = False 
    while(Valid == False): 
        NumberItems = int(input("How many numbers will you enter?")) #loop until < 20 
        if NumberItems > 0 and NumberItems< 21: 
           Valid = True 
    for Count in range(0, NumberItems): 
        DataStored.append(int(input("Enter number")))

                
            

def BubbleSort():
    global DataStored

    top = len(DataStored)
    for i in range(top):
        for j in range(top-1):
            if DataStored[j] > DataStored[j +1]:
                DataStored[j], DataStored[j + 1] = DataStored[j +1], DataStored[j]
        top -= 1

def BinarySearch(DataToFind):
    global DataStored
    global NumberItems
    First = 0 
    Last = NumberItems
    while (First <= Last):
        mid = int((First + Last)/2) 
        if DataToFind == DataStored[mid]:
            return mid
        if DataToFind < DataStored[mid]:
            Last = mid -1
        else:
            First = mid +1 

    return -1

    
    



if __name__ == "__main__":
    global NumberItems
    global DataStored
    DataStored = []
    Initialise()  #integer 
    BubbleSort()  #Integer 20 items 
    print(DataStored)
    usrinp = int(input("What number do you need to search: "))
    print(BinarySearch(usrinp))
