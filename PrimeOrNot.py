def isPrime(data):
    if data == 2:
        print("It is Even and Prime")
    for i in range(2,int(data**0.5)+1):
        print(f"{i} times executed")
        if data % i == 0:
            return False
    return True

#__main__
num=10
print(isPrime(num))