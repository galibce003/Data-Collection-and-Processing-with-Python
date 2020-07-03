#json.loads
import json
a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
d = json.loads(a_string)
print(type(d))
print(d.keys())
print(d['results'])




#json.dumps
import json
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)  #obj will be an dict
                                                      #Sorted and identation will be 2

d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2':{'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(pretty(d))
