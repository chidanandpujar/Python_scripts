#Declaration
list1=[]
list2=["Hello","World"]

#Adding two lists
l1=["a","b"]
l2=["c","d"]
l3=l1+l2
print(l3)

#multiply a list
l1=[1,2]
print(l1*2)

#to check element present in the list
l=["a","b"]
if "a" in l:
    print("present")
else:
    print("absent")

#looping through the list
l=["a","b","c"]
for v in l:
    print(v)
print("Length of list is {}".format(len(l)))

#Copying list
t1=['abc']
print(t1)
t2=t1
print(t2)

#String to list
S="abc"
print(list(S))

#Inserting items
l1=["abc"]
l1.insert(1,"def")
print(l1)

#Sorting and reversing
l1 = [2, 0, 5, 9, 10, 3]
l1.sort()
print(l1)
l1.reverse()
print(l1)
print(max(l1))

#Deleting Elements
l1 = ["Hello", "World"]
del(l1[0])
print(l1)

l2 = ["a","b","c","d"]
del(l2[2:4])
print(l2)
