l1 = [1,2,3]
l2 = [4,5,6]
l3= []

for i in range(len(l1)):
    l3.append(l1[i]+l2[i])
print(l3)



l4 = list(zip(l1,l2))
print(l4)
l5 = []
for (x,y) in l4:
    l5.append(x+y)
print(l5)





#list_comprehension
l6 = [(x+y) for (x,y) in list(zip(l1,l2))]
print("l6 = ",l6)
    
