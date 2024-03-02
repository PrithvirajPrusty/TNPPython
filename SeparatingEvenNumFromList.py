n=input("Enter the numbers into the list:")
m=list(map(int,(n.split(" "))))
print("Original List:",n)
list1=[]
for i in m:
    if i % 2 == 0:
        list1.append(i)
print("Even List:", list1)
