def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        line_number = 1

        for string in strings:
            start_byte = file.tell()
            file.write(string + '\n')
            strings_positions[(line_number, start_byte)] = string
            line_number += 1

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
