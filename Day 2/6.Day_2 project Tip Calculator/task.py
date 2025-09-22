from numpy import around


print("Welcome to the tip calculator!")
bill = float(input("what wa the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10  12 15: "))
people =int(input("how many people to split the bill?"))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = around(bill_per_person, 2)
print(f"each person should pay: $ {final_amount}")





