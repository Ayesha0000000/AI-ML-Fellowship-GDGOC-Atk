numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(set(numbers))
sorted_numbers = sorted(unique_numbers)

print("Unique:", unique_numbers)
print("Sorted:", sorted_numbers)
print("Max:", max(sorted_numbers))
print("Min:", min(sorted_numbers))
print("Average:", sum(sorted_numbers) / len(sorted_numbers))
