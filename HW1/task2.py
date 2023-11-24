def sort_list_imperative(numbers):
  sorted_numbers = sorted(numbers, reverse=True)
  return sorted_numbers

# Пример использования
numbers = [4, 2, 7, 1, 9]
sorted_numbers = sort_list_imperative(numbers)
print(sorted_numbers)