import random
import task1
'''print(random.randint(a=1, b=10))
print(task1.my_phone_number)
random_number = random.randint(a=11, b=20)
print(random_number)

random_number_0_to_1 = random.random()
print(random_number_0_to_1)
random_float_number = random.uniform(1,10)
print(random_float_number)'''
# coin toss game
random_heads_or_tails = random.randint(a=0, b=1)
if random_heads_or_tails == 0:
    print("Head")
else:
    print("Tail")
