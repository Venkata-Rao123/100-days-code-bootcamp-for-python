Height = int(input("Enter your height in cm: "))
if Height >= 120:
   print("can ride")
   age =int(input("Enter your age: "))
   if age <= 12:
      bill = 5
      print(" child ticket price is $5")
   elif age <= 18:
      bill = 7
      print("youth ticket price is $7")
   elif age >= 45 and age <= 55:
      print("Everything is going to be ok. Have a free ride on us!")   
   else:
      bill = 12
      print("adult ticket price is $12")
   wants_photo = input("Do you want a photo taken? Y or N. ")
   if wants_photo == "Y":
      bill += 3
   print(f"Your final bill is ${bill}")
else:
   print("cannot ride")

     
