user_input = list(input("Enter String: "))
arr_no_space = []
for i in range(len(user_input)):
    if user_input[i] != ' ': arr_no_space.append(user_input[i])

lower = ""
upper = ""

for i in range(len(arr_no_space)):
    if arr_no_space[i].upper() == arr_no_space[i]: upper += arr_no_space[i]
    else: lower += arr_no_space[i]


print(lower + upper)
