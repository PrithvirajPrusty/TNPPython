def reverse(N):
    r = 0
    while N != 0:
        rem = N % 10
        r = r * 10 + rem
        N //= 10
    return r
N = int(input("Enter Numbers:"))
print(f"Reverse of {N} is:",reverse(N))