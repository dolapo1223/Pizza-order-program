# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L:  ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N :  ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

#condition for pizza sizes
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25
# condition for add pepperoni or not
if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
#condition for extra_cheese or not
if extra_cheese == "Y":
  bill += 1

#print out final bill
print(f"Your final bill is ${bill}")


   




