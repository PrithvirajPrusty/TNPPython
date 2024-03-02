n=input()
m=list(map(int,(n.split(" "))))
m.sort()
print(m[len(m)-2])