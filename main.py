class GeneratorIterator:
    def __iter__(self):
        def generator():
            n = 0
            while True:
                yield n
                n += 1
        return generator()

iterator_object = GeneratorIterator()

my_generator = iter(iterator_object)

print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))