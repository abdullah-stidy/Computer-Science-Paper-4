NumberArray = [100, 85, 644, 22, 15, 8, 1]

LastItem = 0 
CheckItem = 0 
LoopAgain = False

def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    
    RecursiveInsertion(IntegerArray, NumberElements - 1)
    LastItem = IntegerArray[NumberElements -1]
    CheckItem = NumberElements -2
    
    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    elif IntegerArray[CheckItem] < LastItem:
        LoopAgain = False


    while (LoopAgain):
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem -= 1
        if CheckItem <0:
            LoopAgain = False
        elif IntegerArray[CheckItem] < LastItem:
            LoopAgain = True

    IntegerArray[CheckItem + 1 ] = LastItem
    return IntegerArray

# [100, 85, 644, 22, 15, 8, 1]
def IterativeInsertion(IntegerArray, NumberElements):
    i = 1
    for i in range(1, NumberElements):
        j = i -1
        temp = IntegerArray[i]
        while j >= 0 and IntegerArray[j] > temp:
            IntegerArray[j + 1] = IntegerArray[j]
            j -=1 
        IntegerArray[j + 1] = temp
    return IntegerArray

def BinarySearch(IntegerArray, First, Last, ToFind):

    if First > Last:
        return (f"{ToFind} was Not Found")
    mid = (First + Last)//2


    if ToFind == IntegerArray[mid]:
        return (f"Found it at index {mid}")
    
    if ToFind > IntegerArray[mid]:
        return BinarySearch(IntegerArray, mid + 1, Last, ToFind)

    if ToFind < IntegerArray[mid]:
        return BinarySearch(IntegerArray, First, mid -1, ToFind)
    


Output = RecursiveInsertion(IntegerArray=NumberArray, NumberElements=len(NumberArray))
print("Recursive")
print(Output)

Output = IterativeInsertion(NumberArray, len(NumberArray))
print("Iterative")
print(Output)

Output = BinarySearch(Output, 0, len(NumberArray), 644)
print(Output)