a={'b':1,'a':2,'c':0}
print(a)
print(a['b'])
#a.sort()
b=list(a[x] for x in a)
b.sort()
print (b)
c=list(a)
c.sort()
print(c)
#for name,x in a.items():
    #print (name)
name=list(a.keys())
value=list(a.values())
res={}
for k in b:
    res[name[value.index(k)]] = k
    #print(k)
    '''
    if k in a.values():
        #print(value.index(k))
        #print(name[value.index(k)])
        print (f'{name[value.index(k)]}:{k}')
        res[name[value.index(k)]] = k
        #res=res+f'{name[value.index(k)]}:{k}'
        #print(a.keys())
    '''
#print (b)

mydict = {'george': 16, 'amber': 19}
sa=list(mydict.keys())
sb=list(mydict.values())
#print (b.index(16))
#print(list(mydict.keys())[list(mydict.values()).index(19)])  # Prints george

print(a)
print (res)


resC={}
for k in c:
    resC[k]=a[k]
print (resC)
