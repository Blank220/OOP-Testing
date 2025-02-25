print("Welcome to PRT! ")
print("Select destination:")
stations = [1, 2, 3, 4, 5]
price = 0
tickets = 0

print(stations) 
destination = int(input("")) 

if destination in stations:
  print("How many tickets?") 
  amt = int(input("")) 
  tickets += amt   
else:
  print("Please pick from the list") 

if destination == 1:
  print(f"You have chosen Station number {destination}") 
  price += 10
  price = price * tickets
  print(f"Amount to pay is {price}") 

elif destination == 2:
  print(f"You have chosen {destination}") 
  price += 20
  price = price * tickets
  print(f"Amount to pay is {price}") 

elif destination == 3:
  print(f"You have chosen {destination}") 
  price += 30
  price = price * tickets
  print(f"Amount to pay is {price}") 

elif destination == 4:
  print(f"You have chosen {destination}") 
  price += 40
  price = price * tickets
  print(f"Amount to pay is {price}") 

elif destination == 5:
  print(f"You have chosen {destination}") 
  price += 50
  price = price * tickets
  print(f"Amount to pay is {price}") 

print("Please insert coin or bills to pay")

print("Insert Cash")
cash = int(input("")) 
change = cash - price

if change == 0:
  print("You have no change, here's your ticket")
elif change < 0:
  print("Kulang ka ng bayad tanga")
else:
  print(f"Here's your change and ticket: {change}")
  
print("Thank you, come again!")



 
 
 


  
 
