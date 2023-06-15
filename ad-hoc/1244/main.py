N = int(input())

count = 0

stringsList = []
sortedStringListByLen= []

while count < N:
    stringList = input().split(" ")

    stringList.sort(key=len, reverse=True)

    for index in range(len(stringList)):
        print(stringList[index], end = "")
        if(index != len(stringList) - 1):
            print(" ", end="")
    count += 1
    print()