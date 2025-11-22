while True :
  balance = 10000 
  pin = 1234
  password = "Mohit123@"

  while True:
    try:
      user_pass = input("Enter your password : ")
      if user_pass == password:
        print(f"your password {user_pass.replace("ohit123","*******")} is correct")
      else:
        print("your password is not correct! please try again !")
        continue
    except:
      print("Enter required password ")
      continue

    users_pin = int(input("Enter your Pin : "))
    if users_pin != pin :
      print("Invalid Pin , please try again")
      continue

    elif users_pin == pin:
      while True :  
        amount = int(input("Enter amount to withdraw :"))
        if amount == balance :
          print("we can't withdraw full amount from ATM due to some bank policies")
          print("please withdraw less than ",balance," ?")
          continue
        elif amount > balance :
          print("Insufficient balance")
          print("Available balance :",balance)
          continue
        else:
          balance = balance - amount
          print("Please collect your cash :",amount)
          print("Available balance :",balance)
          print("Do you want to withdraw more ? yes for 'y' and no for 'n'")
          choice = input().lower()
          if choice == 'y':
            continue
          else:   
            print("Thank you for using ATM service")
          break
    break





