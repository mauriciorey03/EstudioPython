import random

random_num=[]

for i in range(10):
    random_num.append(random.randint(0,5))
print(random_num)

nums_ord=sorted(random_num)
print(nums_ord)

nums_ord.sort()