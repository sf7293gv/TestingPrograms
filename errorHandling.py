try:
    with open('data.txt') as data_file:
        contents = data_file.read()
        print(contents)
except FileNotFoundError:
    print('File not found.')