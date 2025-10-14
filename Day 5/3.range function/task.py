# Range function within a for loop
# Example 1: print the number starting  and ending value not inccluding the end value
for number in range(1, 11): # for starting from 1 to 10 (11 is excluded)
    print(number)
# Example 2: print the number starting  and ending values not inccluding the end value with a step value     
for number in range(1, 11, 3): # for starting from 1 to 10 (11 is excluded) with a step of 3
    print(number)
# Example 3: Calculate the sum of numbers from 1 to 100 (including 100) +   
total = 0
for number in range(1, 101): # for starting from 1 to 100 (101 is excluded)
    total += number
print(total)