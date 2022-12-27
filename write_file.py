# запись в файл+ перезапись
with open('resources/example.txt', 'w') as f:
    f.write('Hello, world!\n World hello!\nabc')

# чтение файла
with open('resources/example.txt') as f:
    for row in f:
        print(row)

# создание нового файла с х (в сущ файл не получится)
# with open('example_1.txt', 'w') as f:
#     f.write('Hello, world!\n World hello!')

#создание,если не существует, и дописывание в файл в конец
with open('resources/example_a.txt', 'a') as f:
    f.write('A')

#проверка что-то есть в файле
with open('resources/example.txt', 'r') as f:
    text = f.read()
    assert 'abc' in text