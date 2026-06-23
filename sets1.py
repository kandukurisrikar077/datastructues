s={1,3,4,7,5,6}
l=list(s)
print("list is:",l)
"""temp=l[0]
l[0]=l[5]
l[5]=temp"""
l[0],l[-1]=l[-1],l[0]
print("new list:",l)
s1=set(l) #set always prnts in ordered form
print(s1)
