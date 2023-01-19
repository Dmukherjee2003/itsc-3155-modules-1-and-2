arr1 = []
arr2 = []
arr3 = []
for i in range(0,5):
    number = int(input("Enter a number for first list: "))
    arr1.append(number)

for i in range(0,5):
    number2 = int(input("Enter a number for second list: "))
    arr2.append(number)

for i in range(len(arr1)):
    if arr1[i] in arr2:
        arr3.append(arr1[i])

print("List 1: ", arr1)
print("List 2: ", arr2)
print("List 3: ", arr3)

