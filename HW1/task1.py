def sort_list_imperative(numbers):
  n = len(numbers)
  for i in range(n - 1):
    for j in range(n - 1 - i):
     if numbers[j] < numbers[j + 1]:
      numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
  return numbers

# Пример использования
numbers = [4, 2, 7, 1, 9]
sorted_numbers = sort_list_imperative(numbers)
print(sorted_numbers)