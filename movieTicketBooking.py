age = int(input("Enter your age : "))
ticket = input("Enter 1 for True and 0 for false :")
flage = bool(ticket)
if age >= 18 :
  print("you can watch movie")
  if flage == True:
    print("you can go inside hall")
  else :
    print("you can't go inside the hall")
elif age < 15:
  print("you can go with your parents")
else :
  print("Not allowed")

# NOT key word

ticket = True
if not ticket:
  print("Denied")

# Range function

for i in range(5):
  print("1")

for i in range(2,10):
  print(i)

for i in range(2,10,2):
  print(i)

for j in range(-10,0):
  print(j)

for j in range(-10,0,2):
  print(j)


""" print the star using the * only
2. Write a program that takes a number as input and determine if it's possitive , negative or zero.
3. Write a progrma to check the year is leap year or not. 
4. write a program to print a paligndrome sequence of 8 number.
5. triangle pattern using stars."""


z = int(input("Enter the a number to check it is positive , negative or zero :"))
if z > 0:
  print("The number is positive")
elif z < 0:
  print("The number is negative")
else :
  print("The number is zero")

# whie loop

count = 1
while count <= 5:
  print("Hello World")
  count += 1

print (""" 
       1. Addition
       2. Substration
       3. multiplication
       4. division  
       5. exit""")

# Keep asking until we get a valid integer choice between 1 and 5

while True:
  try:
    print (""" 
       1. Addition
       2. Substration
       3. multiplication
       4. division  
       5. exit""")
    choice = int(input("Enter your choice 1-5 :"))
  except ValueError:
    print("Please enter a valid integer (1-5).")
    continue
  if 1 <= choice <= 5:
    break
  print("Invalid choice, please enter again between 1-5 :")

if choice == 5:
  print("Exiting.")
  exit()

# Only ask for numbers when an arithmetic operation is selected

num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))

if choice == 1:
  print("The addition is :", num1 + num2)
elif choice == 2:
  print("The substration is :", num1 - num2)
elif choice == 3:
  print("The multiplication is :", num1 * num2)
elif choice == 4:
  # guard division by zero
  if num2 == 0:
    print("Error: division by zero is not allowed.")
  else:
    print("The division is :", num1 / num2)



for i in range(1,10):
  if i == 3:
    continue
  print(i)


  # exceptional handling
try:
  a = int(input("Enter first number :"))
  b = int(input("Enter second number :"))
  print("The division is :", a / b)
except:
  print("Error: division by zero is not allowed.")

while True:
    balance = 5000
    pin = 1234
    user_pin = int(input("Enter your pin :"))
    if user_pin == pin:
      print("your balance is :", balance)
      amount = int (input("Enter the amount to withdraw :"))
      balance -= amount
      print("Your remaining balance is :", balance)
    elif user_pin != pin:
       print("Invalid pin")
    else :
      break    
  


