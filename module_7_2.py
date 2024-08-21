def custom_write(file_name, strings):
    strings_positions = {}

    # Открываем файл для записи в текстовом режиме с кодировкой utf-8
    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings, start=1):
            # Получаем текущую позицию в файле
            start_byte = file.tell()
            # Записываем строку с символом новой строки
            file.write(string + '\n')
            # Сохраняем данные в словарь
            strings_positions[(i, start_byte)] = string

    # Возвращаем полученный словарь
    return strings_positions


# Пример использования
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
