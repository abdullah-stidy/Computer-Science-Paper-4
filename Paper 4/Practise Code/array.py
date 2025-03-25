import random
DataArray = [random.randint(1, 10) for i in range(1,50)]

target = int(input("What is the value you want to search \n"))
flag = True
for index, item in enumerate(DataArray):
    if target == item:
        print(f"{target} found at index {index}")
        flag = False
        break
if flag == True:
    print("Not found")



