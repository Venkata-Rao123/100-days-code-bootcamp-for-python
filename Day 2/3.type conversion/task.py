length_of_print_st=print(len(str(1337))) # this will work and convert the integer to a string
print(length_of_print_st) # this will print None because the print() function returns None
print(type(length_of_print_st))
print(type(1223)) # this will print <class 'int'>
print(type("abc")) # this will print <class 'str'>
print(type(str(True))) # this will print <class 'str'>
print(("123") + ("123"))
print(int("123") + int("123"))

print("Number of letters in your name : " + str(len(input("Enter your name: "))))
