numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
count_ = len(numbers)
name = numbers.pop(4)
# TODO заменить значение пропущенного элемента средним арифметическим
number_ = sum (numbers) / count_
numbers.insert(4,(number_))
print("Измененный список:",numbers)
