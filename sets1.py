s1={1,2,3,4}
s2={5,4,3,2}
s1.add(7)
s2.add(7)
print(s1,s2)
s1.update([99,9])
s2.update([99,9])
print(s1,s2)
s2 = s2.difference(s1)
print(s2)
s1.remove(9)
print(s1,s2)
s1=s2.copy()
print(s1,s2)
s2.add(4)
s2.add(12)
print(s1,s2)





"""s={1,3,4,7,5,6}
l=list(s)
print("list is:",l)
temp=l[0]
l[0]=l[5]
l[5]=temp
l[0],l[-1]=l[-1],l[0]
print("new list:",l)
s1=set(l) #set always prnts in ordered form
print(s1)"""
