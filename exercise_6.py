row = int(input("Enter the number of rows: "))
colomn = int(input("Enter the number of columns: "))

for i in range(1,6):
    for j in range(1,6):
        if i == row and j == colomn:
            print(1, end=" ")
        else:
            print(0, end = " ")
    print('')