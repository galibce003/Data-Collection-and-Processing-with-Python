#filter the even num
l = [1,2,3,4,5,6,7,8,9,10]
e = filter(lambda x : x%2==0,l)
list = list(e)
print(list)




#filter the words
#which contains 'o'
lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]
lst2 = filter(lambda x : 'o' in x,lst)
