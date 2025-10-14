
# Example 1: Print each fruit in the list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    print(fruit  +  " pie")
print(fruits)

# Example 2 : print the total score of the student

students_scores = [10, 20, 20]

max_score = 0
total_score = 0
for score in students_scores:
    total_score += score
print(total_score)

# Example 3 : print the max score of the student 
student_scores = [60,80,75,90,55,70]
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
        print(f"The highest score in the class is: {max_score}")  

# Example 4 : print the sum of the student score        
student_scores = [60,80,56,90]
sum_scores = sum(student_scores)
print(sum_scores)    



