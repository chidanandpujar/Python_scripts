#Declation
tup1=()
tup2=("python",2,"Java",3)
tup3=(1,3,5,7)

#Indexing
tup3=(1,3,5,7)
print(tup3[2])
print(tup3[-3])
print(tup3[1:3])
print(tup3[::-1])

#Finding length
print(len(tup3))

#in operator
tup=("C","C++","Java","Python")
choice = input("Enter Language:")
if choice in tup:
    print("Choice available",choice)
else:
    print("No choice for", choice)

#Min and Max functions
t=(1,2,3,4,5)
print(min(t))
print(max(t))
print(len(t))

#Count and Index
print(t.count(1))
print(t.index(3))

#Sorting
print(sorted(t))
print(sorted(t,reverse=True))
