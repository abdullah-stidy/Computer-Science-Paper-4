class Node():
    def __init__(self, theData=0, nextNodeNumber=None):
        self.data = theData
        self.nextNode = nextNodeNumber

def outputNodes(arr, startPointer):
    nextPointer = startPointer
    while nextPointer != -1:
        data = arr[nextPointer].data
        print(data)
        nextPointer = arr[nextPointer].nextNode
    
def addNode(arr, startPointer, emptylist, newdata):
    if emptylist == 0:
        print(f"the list is full cant add {newdata}")
    else:
        pointer = emptylist
        emptylist = arr[pointer].nextNode

        arr[pointer].data = newdata
        arr[pointer].nextNode = -1

        if startPointer == -1:
            startPointer = pointer
        else:
            currentPointer = startPointer
            while arr[currentPointer].nextNode != -1:
                currentPointer = arr[currentPointer].nextNode
            arr[currentPointer].nextNode = pointer

LinkedList = [Node() for _ in range(10)]

LinkedList[0] = Node(1, 1)
LinkedList[1] = Node(5, 4)
LinkedList[2] = Node(6, 7)
LinkedList[3] = Node(7, -1)
LinkedList[4] = Node(2, 2)
LinkedList[5] = Node(0, 6)
LinkedList[6] = Node(0, 8)
LinkedList[7] = Node(56, 3)
LinkedList[8] = Node(0, 9)
LinkedList[9] = Node(0, -1)


startPointer = 0 
emptyPointer = 5


outputNodes(LinkedList, 0)




