def outer():
    name = "Prithviraj"
    def inner():
        nonlocal name
        print(name)
        name = "Prusty"
    inner()
    print(name)
outer()