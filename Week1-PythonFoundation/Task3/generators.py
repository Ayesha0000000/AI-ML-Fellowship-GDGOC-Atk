# Fibonacci Generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print("Fibonacci Series:")
for num in fibonacci(7):
    print(num)


# Custom Range Generator
def custom_range(start, end, step):
    while start < end:
        yield start
        start += step


print("\nCustom Range:")
for i in custom_range(1, 10, 2):
    print(i)
