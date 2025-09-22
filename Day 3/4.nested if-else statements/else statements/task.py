Height = int(input("Enter your height in cm: "))
if Height >= 120:
   print("can ride")
   age =int(input("Enter your age: "))
   if age <= 12:
      print("ticket price is $5")
   elif age <= 18:
      print("ticket price is $7")
   else:
      print("ticket price is $12")
else:
   print("cannot ride")

     
