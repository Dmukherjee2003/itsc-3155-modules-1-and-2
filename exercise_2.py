user_input = input("Enter a word: ")
user_input2 = input("Enter the word suffix: ")

if user_input.endswith(user_input2):
    print("True")
else:
    print("False")