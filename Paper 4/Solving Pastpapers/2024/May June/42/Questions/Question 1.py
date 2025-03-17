#part 1
def ReadWords(filename):
    global WordArray
    global NumberWords
    WordArray = []
    NumberWords = -1
    with open(filename, 'r') as file:
        for item in file:
            NumberWords += 1
            WordArray.append(item.strip().lower())
    file.close()
    Play()

#Part 2
def Play():
    print(f"The Main word is {WordArray[0]}")
    print(f"Numbers of answers is {NumberWords}")
    WordArray[0] = ""
    usr_choice = ""
    numbercorrect = 0
    while usr_choice != "no":
        usr_choice = input("Enter you words: ").lower()
        i = -1
        correct = 0
        if usr_choice == 'no' or usr_choice == 'stop':
            print(f"{round(((numbercorrect/NumberWords) * 100), 2)}% of answers entered")
            for item in WordArray:
                if item != '':
                    print(item)
            break

        else:
            for item in WordArray:
                i += 1
                if usr_choice == item:
                    numbercorrect += 1
                    print(f"{usr_choice} is a correct word.")
                    correct = 1
                    WordArray[i] = ""
            if correct == 0:
                print(f"{usr_choice} is incorrect")





#Main program
Usrinp = (input("Enter Difficulty level: ")).strip().lower()
ReadWords(f"{Usrinp}.txt")






