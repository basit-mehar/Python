'''Requirements (what to do in Python)

Ask the user for their name.

Ask the user for the price of 2 items.

Ask the user for the quantity of each item.

Calculate the total cost.

Show a message with the user’s name and the total amount.

Use variables, operators, input, print, concatenation, and mathematical operations.'''


name = input("Please enter your name: ") #asking user for their name
a,b=map(eval,input("please enter price for banana and apple: ").split()) #asking user for price of 2 items and using map and eval to convert input to numbers
q1,q2=map(int,input("please enter quantity for banana and apple: ").split()) #asking user for quantity of 2 items and using map and int to convert input to integers
total_cost = (a * q1) + (b * q2) #calculating total cost
print("Hello, " + name + "! Your total cost is: $" + str(total_cost)) #displaying message with user's name and total amount