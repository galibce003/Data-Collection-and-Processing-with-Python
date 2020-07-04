#map- Function
def triple(x):
    return 3*x


def triplesuffle(y):
    nl = map(triple,y)
    return list(nl)

v = [1,2,3]
z = triplesuffle(v)
print(z)




#map- Lambda
def five(value):
    new_list = map(lambda u:5*u, value)
    return list(new_list)


b = [8,9,10]
n = five(b)
print(n)





#Create a list
#That will contain the upper case only
abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

l = map(lambda c: c.upper(),abbrevs)
abbrevs_upper = list(l)
print(abbrevs_upper)





#Create a list
#That will contain the upper case only
#But this time 1st 2 letters only
abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

l = map(lambda c: c[:2].upper(),abbrevs)
abbrevs_upper = list(l)
print(abbrevs_upper)






#Same as before
#But using another function
abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]
def tnsfr(x):
    return x.upper()

new = map(tnsfr,abbrevs)
y = list(new)
print(y)




