def is_prime(number):
  
    if number <= 1:
        return False
      
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
          
            return False
    return True

def find_prime(location):
  count = 0
  number = 2
  
  while count < location:
    
    if is_prime(number):
      count += 1
    number += 1
    
  return number - 1

program_running = True

while program_running:
  try:
    print("\n--= Prime Number Tool =--\n")
    modes = ("prime checker", "prime locator")
    calculator_mode = str(input("""\nEnter 'prime checker' to check if a number is prime 
\nor 'prime locator' to find the nth prime in the set of natural numbers: """))
    
    if calculator_mode.lower() not in modes:
      raise ValueError
    
    break
  
  except ValueError:
    print("\nPlease enter one of the calculator modes.")
    
if calculator_mode.lower() == "prime checker":
  
  input_number = int(input("\nEnter the integer to check: "))

  result = is_prime(input_number)
  
  print("\n",result)
  
elif calculator_mode.lower() == "prime locator":
  
  input_number = str(input("\nEnter the value of n to identify the nth prime: "))
  result = find_prime(int(input_number))
  
  if input_number[-1] == "1":
    
    print(f"\nThe {input_number}st prime is {result:,}")
    
  elif input_number[-1] == "2":
    
    print(f"\nThe {input_number}nd prime is {result:,}")
  
  elif input_number[-1] == "3":
    
    print(f"\nThe {input_number}rd prime is {result:,}")
  
  else:
    print(f"\nThe {input_number}th prime is {result:,}")
  

    
