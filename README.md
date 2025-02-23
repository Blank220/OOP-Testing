print("The Multiplication Table")

number = int(input("")) 

for i in range(1,11):
  result = number * i
  print(f"{number} x {i} = {result}")


while True:
    number = int(input("Enter a positive integer: "))
    if number < 0:
      print("That is not a positive integer.Please enter a positive integer.")
    else:
      factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(factorial) 
    break
    
