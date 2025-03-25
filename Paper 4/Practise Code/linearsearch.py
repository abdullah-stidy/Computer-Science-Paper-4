#linear search

def linear_search(arg, target):
    flag = False
    for index, value in enumerate(arg):
        print(index, value)
        if value == target:
            print(f"{value} found in index {index}")
            flag = True
            break

        if flag != True:
            print(f"{value} not found in array")


    
    arg = [12, 23, 12, 3, 3, 5, 6, 1]
    target = 5

    linear_search(arg, target)


