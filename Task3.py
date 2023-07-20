# Створюємо функцію для перевірки чи є число простим
def simple_number(number: int):
    if number == 1 or number == 0:
        return False  # 1 та 0 не є простим чи складним числом
    for i in range(2, int(number ** 0.5) + 1):
        if not number % i != 0:
            return False
    else:
        return True


# Створюємо генератор простих чисел
def generator_simple_number(n: int):
    count = 0
    num = 2
    while count < n:
        if simple_number(num):
            count += 1
            yield num
        num += 1


for num in generator_simple_number(10):
    print(num)

print("-" * 10)

gn = generator_simple_number(10)
print(next(gn))
print(next(gn))
print(next(gn))
print(next(gn))
print(next(gn))
