var = []
var2 = []
state = True
while state == True:
    number = input("Enter a number of QUIT to quit: ")
    if number == "QUIT": 
        state = False
        break
    else: 
        var.append(int(number))

for i in range(len(var)):
    if var[i] % 2 == 0: 
        var2.append(var[i])

print(var)
print(var2)
