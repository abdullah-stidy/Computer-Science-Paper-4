def ReadData():
    array = [
    ["", "", ""] for i in range(7)
    ]
    filename = "HighScoreTable.txt"
    i = 0 
    with open(filename, 'r') as file:
        while True:
            playerid = file.readline().strip()
            if not playerid:
                break
            game_lvl = file.readline().strip()
            score = file.readline().strip()
            array[i] = (playerid, game_lvl, score)
            i +=1
    return array
    

def OutputHighScores(array):
    for i in range(len(array)):
        player, game, score = array[i]
        print(f"{player} reached level {game} with a score of {score}")


def SortScores(array):
    top = len(array)

    for i in range(top):
        for j in range(top - 1):
            if array[j][1] < array[j+1][1]:
                array[j], array[j+1] = array[j +1], array[j]

        top -= 1
    return array        






if __name__ == "__main__":
    HighScores = [
    ["", "", ""] for i in range(7)
    ]

    HighScores = ReadData()
    print("Before")
    OutputHighScores(HighScores)
    HighScores = SortScores(HighScores)
    print("After")
    OutputHighScores(HighScores)


