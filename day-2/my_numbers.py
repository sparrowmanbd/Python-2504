# salary=5000
# overtime=500
#all user input recognised as string
#user input
name=input("Enter your name")
# salary=int(input("Enter your salary"))
# overtime=int(input("Enter your overtime total"))

salary=float(input("Enter your salary"))
overtime=float(input("Enter your overtime total"))

#process
total_salary=salary+overtime


#output
print(f"Welcome {name}, you have received your total_salary accumulated with overtime, the amount is {total_salary}")