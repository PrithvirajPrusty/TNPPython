def generate_func():
    yield "Yield"
    yield "Keyword"
    yield "in"
    yield "Python"

generator_object = generate_func()
print(type(generator_object))
for i in generator_object:
    print(i)