
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
  