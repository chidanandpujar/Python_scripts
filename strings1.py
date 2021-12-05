#strings declaration
str1 = "Hello"
str2 = "Hello"

#Length of strings
print(len(str1))

#Concatenation
s1 = "Hi\t"
s2 = "Python"
print(s1+s2)

#Replacement
s='abcd'
print(s)
s=s.replace("cd","cz")
print(s)

#Strings split
s="Strings are needed"
print(s)
s=s.split()
print(s)
s="aabaabaa"
print(s)
s=s.split("b")
print(s)

#split based on count
s="aabaabaa"
s=s.split("b",1)
print(s)

#count substrings
s="aaabbbbbaaa"
print(s)
s=s.count('a',0,5)
s="aaabbbbbaaa"
print(s)
s=s.count('a',0,len(s))
print(s)
