size = 10
class Node():
    def __init__(self):
        self.data = ""
        self.left = None
        self.right = None

def IntializeTree():
    global Tree, Freepointer, Rootpointer

    Tree = [Node() for i in range(size)]

    for i in range(size-1):
        Tree[i].left = i + 1

    Freepointer = 0 

def FindInsertionPoint(Data):
    Pointer = Rootpointer

    while Pointer is not None:
        Current = Tree[Pointer].data
        PrevPointer = Pointer

        if Current > Data:
            Direction = "Left"
            Pointer = Tree[Pointer].left
        else:
            Direction = "Right"
            Pointer = Tree[Pointer].right
    return PrevPointer, Direction


def AddNode(NewDataItem):
    global Tree, Freepointer, Rootpointer

    if Freepointer is None:
        print(f"The Tree is full delete node before you add {NewDataItem}")
        return
    else:
        NewPointer = Freepointer
        Tree[NewPointer].data = NewDataItem
        Freepointer = Tree[NewPointer].left
        Tree[NewPointer].left = None
        print(f"Added {NewDataItem} to the Tree")

        if Rootpointer is None:
            Rootpointer = NewPointer
        else:
            Pointer, Direction = FindInsertionPoint(NewDataItem)

            if Direction == "Left":
                Tree[Pointer].left = NewPointer
            elif Direction == "Right":
                Tree[Pointer].right = NewPointer
            
def TranverseTree(Pointer = None):
    if Pointer is  None:
        Pointer = Rootpointer
    left = Tree[Pointer].left
    right = Tree[Pointer].right
    Data = Tree[Pointer].data

    if left is not None:
        TranverseTree(left)
    print(Data)
    if right is not None:
        TranverseTree(right)


def DeleteNode(Data):





        










if __name__  == "__main__":

    Tree = []
    Freepointer = None
    Rootpointer = None


    Animals = [
        "Mouse",
        "Cat",
        "Toger",
        "Giraage",
        "Dog",
        "Lion",
        "Bird",
        "Snake",
        "Goat",
        "Cow",
        "New",
        "Check",
        "Cheaa"
    ]

    IntializeTree()

    for item in Animals:
        AddNode(item)

    TranverseTree()
