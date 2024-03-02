List = input("Enter Numbers in the List:").split()
n = list(map(int, List))
print(n)
sum = 0
for i in range(0,len(n)):
    sum += n[i]
print("Sum:",sum)