#even odd number
number=int(input("Enter a number"))
if number%2==0:
    print("Even number")

else:

    print("Odd number")

#leap year
year=int(input("Enter a year:"))

if (year%4==0 and year%100!=0 or year%400==0):
   
   print("Leap year")

else:
    print("Not leap year")

