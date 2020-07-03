import copy  #for deepcopy function
l = [[1,2,3],[4,5,6]]
shallow_copy = l[:]
deep_copy = copy.deepcopy(l)


l.append([44,55,66])


print(l)
print(shallow_copy)
print(deep_copy)
