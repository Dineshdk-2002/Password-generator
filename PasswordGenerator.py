# password generator
import random
import string
def password_generator():

  letters = int(input("How many letters would you like in your password ? "))

  symbols = int(input("How many symbols would you like? "))

  numbers = int(input("How many numbers would you like? "))

  random_letters = "".join(random.choice(string.ascii_letters) for i in range(letters))

  num = ["1","2","3","4","5","6","7","8","9","0"]
  random_number = "".join(random.choice(num)for j in range(numbers))

  symbol_lst = ["!","@","#","$","%","^","&","*","(",")","_","-","+","=","<",">","?"]
  random_symbol = "".join(random.choice(symbol_lst)for k in range(symbols))


  print("Your password : ",str(random_letters)+str(random_symbol)+str(random_number))
