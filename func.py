func1 = lambda names: [print(i) for i in names if "a" in i.lower()]

names = input("Enter names: ").split(",")
func1(names)

"""def add(*args): #variable length
    s=0
    for ele in args:
        s+=ele
    return s
print(add(10,20,30))"""