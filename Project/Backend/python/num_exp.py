try:
    divisor = int(input("Enter Divisor: "))
    divider = int(input("Enter Divider: "))
    
    result = divisor / divider
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    
except ValueError:
    print("Error: Please enter valid integers.")
