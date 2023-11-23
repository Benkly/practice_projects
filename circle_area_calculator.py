import math

print("""        Circle area calculator
      ___________________________\n
      """)

while True:
    try:
        radius = float(input("Enter the circle's radius: "))
        if radius >= 0:
              break
        else:
              print("\nThe radius must be a positive real number!\n")
              continue
    except ValueError:
        print("\nThe radius must be a positive real number!\n")

area = round(math.pi * (radius)**2, 2)

print(f"\nThe area of a circle with radius {radius} is {area}\n")

