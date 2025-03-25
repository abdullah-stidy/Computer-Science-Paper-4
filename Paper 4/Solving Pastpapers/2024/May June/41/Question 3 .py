def Enqueue(NewData):
    global QueueData, QueueHead, QueueTail

    if QueueTail == 19:
        return False
    else:
        QueueTail += 1
        QueueData[QueueTail] = NewData
        return True
def Dequeue():
    global QueueData, QueueHead, QueueTail
    if QueueHead == QueueTail:
        return False
    else:
        QueueHead += 1
        return QueueData[QueueHead]
    
def StoreItem():
    global QueueTail, QueueData, QueueTail, QueueHead
    count = 0

    for i in range(10):
        string = input("Enter the number: ")
        checknum = string[5]
        if checknum == 'X':
            checknum = 10
        else:
            checknum = int(checknum)
        

        sum = (int(string[0]) + int(string[2]) + int(string[4])) + ((int(string[1]) + int(string[3]) + int(string[5]))* 3)
        checkdigit = int(sum/10)

        if checkdigit == int(string[5]):
            stat = Enqueue(string[:6])
            if stat == False:
                print(f"Queue is full cant add {string}")
            else:
                print(f"The digit is valid and has been added. {string}")
        else:
            count += 1
    print(f"there were {count} items")







if __name__ == "__main__":
    QueueData = ["" for i in range(20)]
    QueueHead = -1 
    QueueTail = -1
    count = 0 
    StoreItem()
    stats = Dequeue()
    if stats == False:
        print("The Queue is empty.")
    else:
        print(stats)




