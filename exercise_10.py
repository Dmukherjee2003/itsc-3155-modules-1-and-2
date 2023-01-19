arr = []
arr2 = []
word = input("Enter a Word: ")
stringList = list(word)
for i in range(len(stringList)):
    arr2.append(stringList[i])
    if (i+1) % 3 == 0:
        arr.append(arr2)
        arr2 = []
if arr2:
    arr.append(arr2)
print(arr)