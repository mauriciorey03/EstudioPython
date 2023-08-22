import random

def binary_search(data, target, low_ind, high_ind):
    if low_ind > high_ind:
        return False
    mid = (low_ind + high_ind) // 2
    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data,target, low_ind,high_ind, mid-1)
    else:
        return binary_search(data,target, mid+1, high_ind)

data = [random.randint(0,100) for i in range(10)]
print(data)
data.sort()
print(data)
target = int(input('What number do you like to find?'))
found = binary_search (data,target,0, len(data)-1) #Nuestros datos, el objetivo, ind ini, ind final)
print(found)

