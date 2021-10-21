#testar kod
import random

def my_custom_random():
  exclude=[2,5,7,1,8,3,4,6]
  randInt = random.randint(0,9)
  return my_custom_random() if randInt in exclude else randInt 

print(my_custom_random())