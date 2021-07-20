numbers = [8, 9, 10, 11]
numbers.insert(1, 17)
numbers.pop(2)
numbers.insert(len(numbers) + 1, 4)
numbers.insert(len(numbers) + 1, 5)
numbers.insert(len(numbers) + 1, 6)
numbers.pop(0)
numbers += numbers
numbers.insert(3, 25)
print(numbers)