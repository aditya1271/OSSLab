def num (n) :
    return n * 2
old=[1,2,3,4,5,6,7,8,9,10]        
new = [num(x) for x in old]
print(list(new)) 