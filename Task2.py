numbers = [i for i in range(1, 10)]


# Використовуючи генератор
def generator(numbers: list):
    generator_index = 0
    while generator_index != len(numbers):
        if not numbers[generator_index] % 2:
            yield numbers[generator_index] ** 2
        generator_index += 1


result_generator = [num for num in generator(numbers)]
print(result_generator)

# Тут я зрозумів, що можна було не придумувати generator а просто використати List comprehension
result_generator = [num ** 2 for num in numbers if not num % 2]
print(result_generator)

# Використовуючи цикл
result_cycle = []
for num in numbers:
    if num % 2 == 0:
        result_cycle.append(num ** 2)

print(result_cycle)
