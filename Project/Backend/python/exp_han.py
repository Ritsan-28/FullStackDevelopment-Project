first_name = input("Enter First Name: ")

if first_name.isalpha():
    print("You entered:", first_name)
else:
    print("Error: Name must contain only letters (no digits or special characters).")
