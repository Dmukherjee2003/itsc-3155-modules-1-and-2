user_input = int(input("Enter a number: "))
number = 0
arr = []
for i in range(user_input):
    number = float(input("Enter a number: "))
    average = number + number
    arr.append(number)
average = average/user_input
print("List:",arr)
print("Average: ", average)


    