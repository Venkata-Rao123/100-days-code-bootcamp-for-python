'''import random
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
print(fruits)
print(fruits[0]) # accessing the first item
print(fruits[-1]) # accessing the last item
print(fruits[2:5]) # accessing items from index 2 to 4
print(fruits[:3]) # accessing items from the start to index 0 to 2
print(fruits[3:]) # accessing items from index 3 to the end
fruits.append("grape") # adding an item to the end of the list
print(fruits)
fruits.extend(["mango", "pineapple"]) # adding multiple items to the end of the list
print(fruits)
fruits.insert (5, "blueberry") # adding an item at a specific index
print(fruits)
# option 1
print(random.choice(fruits))
# option 2
random_index = random.randint(a=0, b=6)
print(fruits[random_index])
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts",
                     "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina"]
Num_of_states = len(states_of_america)
print(Num_of_states)
print(states_of_america[Num_of_states -1])'''
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
vegetables = ["tomato", "potato", "cabbage", "celery", "carrot"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1])
