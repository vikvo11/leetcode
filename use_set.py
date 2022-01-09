

# Sorting list of Integers in ascending


asd=[11,22,33,9]
ask=[22,33,12,5,1,2,3,9,1]
a=list(set(ask))
print (a)
a.sort(reverse=False)
ask.sort()
print(a)
print(f'ask sort {ask}')
#print(f'ask sort {list(set(ask)).sort()}')
#b=[3,1,2,5,7,13,9,7,5,3,2,1,3,2,9]
b=[33,44,3,1,2,5,7,13,9,7,7,3]
c=[1,2,3,18,11,15]
#print (f"the B value is = {b}")
#print ('hello a %s'% list(a)[0])
for x,i in enumerate(asd):
    asd[x]=int(i)
    #print (a.get(i))
    #print (x)
#print (a)
#print (set(a))
print(f'asd={asd}')
print(f'set asd={set(asd)}')
#print (set(b))
k=list(set(b))

#print (k)
set1=set(b)
set2=set(c)
set1.update(set2)
#print (set1)
'''
t={'N_'+str(v):v for v in c if v not in b}
for v in c:
    print(v)
    if v not in b:
        print ('not')
'''
#print (TT)
#print (f"t={t}")
#print (list(b-set(b)))
#print (c)
#print (set(c))
#print({v for v in c if v not in b})
#[item for item in x if item not in y]
test={v for v in b if v not in c}
#b.remove(test)
#print (test)

print (f'set b = {list(set(b))}')
print (f'b = {b}')
#print (b.remove(13))
'''
if 13 in b:
    b.remove(13)
    print (b)
'''
def test(i):
    aaa=list(i)
    #sort_aaa=list(set(i))
    #sort_aaa.sort()
    for k in list(set(i)):
        if k in aaa:
            aaa.remove(k)
    n=[]
    #aaa.sort()

    for k in list(set(i)):
        n.append(k)
        for t in aaa:
            if t==k:
                n.append(t)
        #print (n)
    n.sort()
    return n

aa=list(b)
for k in list(set(b)):
    if k in aa:
        aa.remove(k)

#print (aa)
'''
n=[]
for k in list(set(b)):
    n.append(k)
    for t in aa:
        if t==k:
            n.append(t)
    print (n)
'''

####
a = [10, 20, 30, 40, 20, 30, 40, 20, 70, 20]
a = [x for x in a if x != 20]
#print(a)
#print (test(b))
print (aa)
#print (set(aa))
print (test(b))
