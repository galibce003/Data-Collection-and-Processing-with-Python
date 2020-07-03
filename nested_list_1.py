nested1 = [[1,2,3],[4,5,6],[7,8,9]]    #each of the item is a list

print(nested1[0])                      #return item no 0

print(len(nested1))

nested1.append([10,11,12])
print(nested1)


nested1[0].append(567)   #I can index more as much as I want to specify the location
print(nested1)



for x in nested1:        #print every list of that list
    print(x)
    

for x in nested1:        #print every item of that list of the main list
    for y in x:
        print(y)


nested1[3] = [55,66,77]  #Replace
print(nested1)


nested1[0][2] = 4        #Replace
print(nested1)



nes2 = [{"a":1,"b":2},{"c":3,"d":4},{"e":5,"f":6}]    #each of the item is a dict
print(nes2[1])
