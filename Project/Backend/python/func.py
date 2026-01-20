def vote(age):
    if(age>17):
        print("Eligible to vote.")
    else:
        print("Not Eligible to vote.")

age = int(input("Enter Age : "))
vote(age)