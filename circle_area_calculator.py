from math import pi
from decimal import Decimal

print("""\n        Circle area calculator
      ___________________________\n
      """)

program_running = True
pi = Decimal.from_float(pi)

while program_running:
    try:
        radius = Decimal.from_float(float(input("Enter the circle's radius: ")))
        decimal_places = int(input("Enter the number of decimal places to round to: "))
        if radius >= 0 and decimal_places >= 0:
              break
        elif radius < 0: 
          print("\nThe radius must be a positive real number!\n")
        elif decimal_places < 0:
          print("\nThe number of decimal places must be a natural number!\n")
        continue
    except ValueError:
        print("\nYou must enter a number!\n")

if decimal_places > 0:
  area = round((pi * (radius)**2), decimal_places)
  
else: 
  area = (pi * (radius)**2)

print(f"\nThe area of a circle with radius {radius} units is {area} units squared\n")