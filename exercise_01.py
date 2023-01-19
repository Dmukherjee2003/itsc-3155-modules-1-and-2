user_input = int(input("Enter a grade: "))
if user_input <= 100 and user_input >= 90:
    print("your grade is: A")
elif user_input >= 80 and user_input <= 89:
    print("your grade is: B")
elif user_input >= 70 and user_input <= 79:
    print("your grade is: C")
elif user_input >= 60 and user_input <= 69:
    print("your grade is: D")
elif user_input >= 0 and user_input <= 59:
    print("your grade is: F")