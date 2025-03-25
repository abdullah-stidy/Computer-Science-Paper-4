class Tree():
    def __init__(self, pTreeName, pHeightGrowth, pMaxHeight, pMaxWidth, pEvergreen):
        # declare Treename:String 
        # DECLARE HeightGrowth: INTEGER
        # DECLARE MaxHeight: INTEGER
        # DECLARE MaxWidth: INTEGER
        # DECLARE Evergreen: STRING 

        self.__TreeName = pTreeName
        self.__HeightGrowth = pHeightGrowth
        self.__MaxHeight = pMaxHeight
        self.__MaxWidth = pMaxWidth
        self.__Evergreen = pEvergreen


    def GetTreeName(self):
        return self.__TreeName
    

    def GetGrowth(self):
        return self.__HeightGrowth
    

    def GetMaxHeight(self):
        return self.__MaxHeight
    

    def GetMaxWidth(self):
        return self.__MaxWidth
    

    def GetEvergreen(self):
        return self.__Evergreen
        
def ReadData():
    filename = "Trees.txt"
    TreeArray = [] #type tree
    i = 1
    try:
        with open(filename, 'r') as file:
            while True:
                line = file.readline()
                if line == "":
                    break
                TreeName, HeightGrowth, MaxHeight, MaxWidth, Evergreen = line.split(',')
                Treeobj = Tree(TreeName, HeightGrowth, MaxHeight, MaxWidth, Evergreen)
                TreeArray.append(Treeobj)
                i += 1
    except FileNotFoundError:
        print("File not found, Error")
    return TreeArray

def PrintTress(TreeObject):
    TreeName = TreeObject.GetTreeName()
    HeightGrowth = TreeObject.GetGrowth()
    MaxHeight = TreeObject.GetMaxHeight()
    MaxWidth = TreeObject.GetMaxWidth()
    Evergreen = TreeObject.GetEvergreen()
    Evergreen = Evergreen.lower().strip()
    

    if Evergreen.lower() == "no":
        print(f"{TreeName} has a maximun height {MaxHeight} a maximum width {MaxWidth} and grows {HeightGrowth} cm a year. It does loses it leaves each year.")
    else:
        print(f"{TreeName} has a maximun height {MaxHeight} a maximum width {MaxWidth} and grows {HeightGrowth} cm a year. It does not loses it leaves each year.")


                                     
def ChooseTree(array):
    usrHeight = int(input("Enter  maximum height the tree in cm: "))
    usrWidth = int(input("Enter maximum width the tree in cm: "))
    usrEvergreen = input("Do you want evergreen??? Yes or No: ").strip().lower()

    usrTree = []
    for i in range(len(array)):
        MaxHeight = int(array[i].GetMaxHeight())
        MaxWidth = int(array[i].GetMaxWidth())
        Evergreen = array[i].GetEvergreen().strip().lower()

        if (MaxHeight <= usrHeight) and (MaxWidth <= usrWidth) and (Evergreen == usrEvergreen):
            usrTree.append(array[i])
            PrintTress(array[i])

    usrchoice = input("Enter the name of the tree you want to buy: ").lower().strip()
    CurrentHeight = int(input("Enter  the height of the tree in cm when it is bought: "))
    for i in range(len(usrTree)):
        Treename = usrTree[i].GetTreeName().strip().lower()
        if usrchoice == Treename:
            MaxHeight = int(array[i].GetMaxHeight())
            Growth = int(array[i].GetGrowth())
            years = int((MaxHeight - CurrentHeight)/Growth) + 1
            print(f"The {Treename} will take {years} years to reach ots max ehight of {MaxHeight}")




        
if __name__ =="__main__":
    TreeArray = ReadData()
    PrintTress(TreeArray[0])
    ChooseTree(TreeArray)