from random import randint
list1 = []
list2 = []
list3 = []
n = 0

for i in range(0,3):
    list1.append(randint(0, 10))
    list2.append(randint(0, 10))
    list3.append(list1[i]+list2[i]) 

print(list1)
print(list2)
print(list3)
