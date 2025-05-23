'''
1. Write a program which will find all such numbers that are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included). The numbers should be printed on the output screen.


for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        print(num, end=' ')
'''


'''
2. Write a program that can compute the factorial of a given number. The number whose factorial is to be
computed is input from the keyboard.


num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial doesn't exist for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of", num, "is", factorial)
'''



'''
3. With a program to take as an input an integer number n, and generate a dictionary that contains (i, i*i)
where “i” lies between 1 and n (both included). The program should then print the dictionary.


n = int(input("Enter a number: "))
square = {}
for i in range(1, n+1):
    square[i] = i*i
print(square)
'''


'''
4. Write a program that can accept two strings as input and print the string with maximum length as an
output. If two strings have the same length, then the program should print both the strings.


str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if len(str1) > len(str2):
    print("The string with maximum length is:", str1)
elif len(str2) > len(str1):
    print("The string with maximum length is:", str2)
else:
    print("Both strings have the same length and are of length", len(str1))
    print("String 1:", str1)
    print("String 2:", str2)
'''


'''
5. Write a program which can produce a dictionary where the keys are numbers between 1 and 20 (both
included) and the values are the square of keys. The program should print the values only.

    squares = {}
for i in range(1, 21):
    squares[i] = i * i
print(list(squares.values()))
'''


'''
6. Write a program which can generate and print a list where the values are square of numbers between 1 and
   20 (both included).

squares = []
for i in range(1, 21):
    squares.append(i * i)
print(squares)
'''


'''
7. Write a program which can generate a list where the values are square of numbers between 1 and 20
(inclusive). The program should only print the last 5 elements of the list.


squares = []
for i in range(1, 21):
    squares.append(i * i)
print(squares[-5:])
'''


'''
8. Write a program to convert Celsius (C) values into Fahrenheit (F). The program should ask for Celsius
value from the user and print the Fahrenheit value as an output.
Formula to Convert Celsius o Fahrenheit: [ F = C * ( 9 / 5 ) + 32 ]




celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit: ", fahrenheit)
'''



'''
9. Write a program which accepts a string as input from the keyboard. If the input string is "even" or
"EVEN" or "Even", print the even numbers from the list (my_numbers) given below. If the string is "odd" or
"ODD" or "Odd", print the odd numbers from the list. Otherwise simply print “Unknown Input!”

my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
input_str = input("Enter 'even' or 'odd': ")
if input_str.lower() == "even":
    even_numbers = [num for num in my_numbers if num % 2 == 0]
    print(even_numbers)
elif input_str.lower() == "odd":
    odd_numbers = [num for num in my_numbers if num % 2 != 0]
    print(odd_numbers)
else:
    print("Unknown Input!")
'''



    
'''
10. Write a program that prints the numbers from 1 to 20. But for multiples of three print “Fizz” instead of
the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and
five print “Fizz Buzz”.


for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
'''
