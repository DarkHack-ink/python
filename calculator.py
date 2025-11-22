from calculator_funct import sum
from calculator_funct import multiply
from calculator_funct import divide
from calculator_funct import substract
from unit_conversion_fun import centimeter_to_meter
from unit_conversion_fun import meter_to_kilometer
from unit_conversion_fun import inches_to_feet
from unit_conversion_fun import inches_to_centimeter


print("Do you want to perform Arithmatic operations or unit converstion \n press 1 to perform Arithmatic Operation \n press 2 to perform unit converstins : ")
choice = int(input("Enter (1/2) : "))

if choice == 1:  
  while True:
    print("- - - - Calculator - - - -")
    print("1. Addition")
    print("2. Subtraction")   
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
      choice = int(input("Enter your choice (1 to 5) :"))
    except :
      print("Invalid input. Please enter a number between 1 and 5.")
      continue
  
  
    if choice == 1:
      while True:
        num1 = float(input("Enter first number :"))
        num2 = float(input("Enter second number :"))
        total = sum(num1, num2)
        print("The addition is :", total)
        try:
          know = input("Do you want to perform addition again (yes/no)").lower()
          if know == "yes":
            continue
          else:
            break
        except:
          print("Invalid input. Exiting addition.")
          break

    elif choice == 2:
      while True:
        num1 = float(input("Enter first number :"))
        num2 = float(input("Enter second number :"))
        subtraction = substract(num1, num2)
        print("The subtraction is :", subtraction)
        try:
          know = input("Do you want to perform subtraction again (yes/no)").lower()
          if know == "yes":
            continue
          else:
            break
        except:
          print("Invalid input. Exiting subtraction.")
          # Removed invalid except block
  
    elif choice == 3:
      while True:
        num1 = float(input("Enter first number :"))
        num2 = float(input("Enter second number :"))
        multiplication = multiply(num1, num2)
        print("The multiplication is :", multiplication)
        try:
          know = input("Do you want to perform multiplication again (yes/no)").lower()
          if know == "yes":
            continue
          else:
            break
        except:
          print("Invalid input. Exiting multiplication.")
          break
  
    elif choice == 4:
      while True:
        try:
          num1 = float(input("Enter first number :"))
          num2 = float(input("Enter second number :"))
          division = divide(num1, num2)
          print("The division is :", division)
          know = input("Do you want to perform division again (yes/no)").lower()
          if know == "yes":
            continue
          else:
            break
        except ZeroDivisionError:
          print("Error: Division by zero is not allowed.")
          break
        except ValueError:
          print("Invalid input. Please enter a valid number.")
          break
  
    elif choice == 5:
      print("Exiting the calculator.")
      break
    else:
      print("Invalid choice. Please enter a number between 1 and 5.")
      break

elif choice == 2:
  while True:

    try:
      user_input = int(input("press 1 to cente meter to meter converstion \n press 2 to meter to kilometer conversion \n press 3 to inches to feet \n press 4 to inches to centimeter \n press 5 celcius to farenhite \n Enter a number :"))
    except :
      print("Invailid Input please enter 1-5 :")
      continue

    if user_input == 1:
      num1 = float(input("Enter a centemeter:"))
      meter = centimeter_to_meter(num1)
      print(f"your meter is {meter} of {num1}")
      break

    elif user_input == 2:
      num1 = float(input("Enter a meter:"))
      kilometer = meter_to_kilometer(num1)
      print(f"your kilometer is {kilometer} of {num1}")
      break
      
    elif user_input == 3:
      num1 = float(input("Enter a inches :"))
      feet = inches_to_feet(num1)
      print(f" your kilometer is {feet} of {num1}")
      break

    elif user_input == 4:
      num1 = float(input("Enter a inches:"))
      centimeter = inches_to_centimeter(num1)
      print(f"your kilometer is {centimeter} of {num1}")
      break
    
    elif user_input == 5:
      num1 = float(input("Enter a celsius:"))
      faurenhite = inches_to_centimeter(num1)
      print(f" your kilometer is {faurenhite} of {num1}")
      break
    
    else:
      print("Exiting the program")
    break
else :
  print("Enter valid number")

  

      
