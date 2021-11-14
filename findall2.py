import re
S = "aabbaa"
P = "a"
for pat in re.findall(P,S):
    print("found",pat)
