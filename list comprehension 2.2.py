#normal for loop
l = [1,2,3,4,5,6,7,8,9,10]
sqr = []
for i in l:
    sqr.append(i**2)
print(sqr)





#by list comprehension
l = [1,2,3,4,5,6,7,8,9,10]
sqr1 = [i**2 for i in l]   #i**2 = transformer expression
print(sqr1)





#by lambda
l = [1,2,3,4,5,6,7,8,9,10]
sqr3 = map(lambda i : i**2,l)
print(list(sqr3))






tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
dict = tester['info']
import json
x = json.dumps(tester, indent = 2)
print(x)      #it will show how the items are arranged
              #for better view(tree), use 'jsoneditoronline.org'
              #just paste the output of print(x)
       
compri= [i['name'] for i in dict]
print(compri)
