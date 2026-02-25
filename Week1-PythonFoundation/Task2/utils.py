def add_numbers(*args):
    return sum(args)


def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


square = lambda x: x * x
