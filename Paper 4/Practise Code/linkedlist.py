class Node():
    def __init__(self):
        self.Data = ""
        self.Pointer = None




def CreateList():
    global List, Headpointer, Freepointer

    List = [Node() for i in range(10)]

    for i in range(9):
        List[i].Pointer = i + 1

    List[9].Pointer = None
    Freepointer = 0 
    Headpointer = None

def AppendList(Newdata:str):
    global List, Headpointer, Freepointer

    if Freepointer is None:
        print("This cant be  aadded the list is full")
    else:
        NewPointer = Freepointer
        Freepointer = List[NewPointer].Pointer

        List[NewPointer].Data = Newdata
        List[NewPointer].Pointer = None

        if Headpointer is None:
            Headpointer = NewPointer
        else:
            Pointer = Headpointer
            while List[Pointer].Pointer is not None:
                Pointer = List[Pointer].Pointer
            
            List[Pointer].Pointer = NewPointer

        print(f"{Newdata} has been added.")



def Prepend(NewData):
    global List, Headpointer, Freepointer

    if Freepointer is None:
        print("This cant be  aadded the list is full")
    else:
        NewPointer = Freepointer
        Freepointer = List[NewPointer].Pointer

        List[NewPointer].Data = NewData
        List[NewPointer].Pointer = None

        if Headpointer is None:
            Headpointer = NewPointer
        else:
            SCPointer = Headpointer
            Headpointer = NewPointer
            List[NewPointer].Pointer = SCPointer


        print(f"{NewData} has been added.")


    





def DisplayList():
    global List, Headpointer, Freepointer
    Pointer = Headpointer
    while Pointer is not None:
        print(List[Pointer].Data, end=", ")
        Pointer = List[Pointer].Pointer
    print("None")




CreateList()
AppendList("China")
DisplayList()
AppendList("Pakistan")
DisplayList()
Prepend("US")
DisplayList()
