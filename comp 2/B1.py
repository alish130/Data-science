numbers = [1, 2, 3, 4, 5]
list_one = numbers
list_one.append(6)
print(numbers) 
print(list_one) 
list_two = numbers[:]
list_two.append(7)
print(numbers) 
print(list_two)  
