arr1 = []
arr2 = []
arr3 = []
for i in range(0,10):
    number = int(input("Enter number: "))
    arr1.append(number)


for i in range(len(arr1)):
    count = 0
    if arr1[i] not in arr3: 
        for j in range(i+1 , len(arr1)):
            if arr1[i] == arr1[j]: 
                count += 1

        if count == 0: 
            arr2.append(arr1[i])
        else: 
            arr3.append(arr1[i])
    
        
print(arr1)
print(arr2)