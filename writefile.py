numbers = ['one', 'two']

with open('numbers.txt', 'w') as number_file:
    number_file.writelines(numbers)