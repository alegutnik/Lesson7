numbers = [i for i in range(1, 10)]


def generator_reverse(numbers: list):
    generator_index = len(numbers)
    while generator_index:
        generator_index -= 1
        yield numbers[generator_index]


for num in generator_reverse(numbers):
    print(num)
