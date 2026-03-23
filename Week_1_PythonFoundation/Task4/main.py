from modules.calculator import add, multiply
from modules.file_utils import write_file, read_file
from mypackage import square, reverse_string

print("Add:", add(5, 3))
print("Multiply:", multiply(4, 2))

write_file("sample.txt", "Hello Fellowship")
print("File Content:", read_file("sample.txt"))

print("Square:", square(5))
print("Reverse:", reverse_string("python"))
