def sum(*args):
  total = 0
  for num in args:
    total = total + num
  return total 
  
# print(sum(1,2,3,4,5))

def multiply(*args):
  result = 1
  for num in args:
    result = result * num
  return result

# print(multiply(1,2,3,4,5))

def divide(*args):
  result = 1
  for num in args:
    result = result / num
  return result

# print(divide(100,2,5))

def substract(*sub_args):
  result =sub_args[0]
  for num in sub_args[1:]:
    result = result - num
  return result

