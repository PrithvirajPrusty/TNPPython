s1,s2,s3 = map(int, input("Enter # sides of the Triangle:").split())
if (s1+s2 > s3 and s1+s3 > s2 and s2+s3 > s1):
    print("Yes")
else:
    print("No")