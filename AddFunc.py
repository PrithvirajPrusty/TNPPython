def add(a:int=4,b:int=5):
    if isinstance(a,int) and isinstance(b,int):
        print(f"{a} + {b}")
    else:
        print(f"Error {a}->{type(a)},{b}->{type(b)}")
add(b=0)