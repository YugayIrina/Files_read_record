import os


# Создадим функцию для работы с заданными файлами
def create_file_list(folder):
    file_list = os.listdir(folder)  # Получаем список имен файлов в папке
    join_file_list = []  # Создаем список для хранения содержимого файлов
    for file in file_list:
        with open(folder + "/" + file) as _temp_file:  # Поочередно считываем файлы
            # Добавляем в список название файла, значение для числа строк и список для содержимого файла
            join_file_list.append([file, 0, []])
            for line in _temp_file:
                join_file_list[-1][2].append(line.strip())  # Добавляем в список содержимое файла построчно
                join_file_list[-1][1] += 1  # Увеличиваем значение для числа строк
    # Возвращаем предварительно отсортированный по значению числа строк список с содержимым файлов
    return sorted(join_file_list, key=lambda x: x[1], reverse=False)


# Создадим функцию для записи итогового файла
def create_join_file(folder, filename):
    with open(filename + '.txt', 'w+') as join_file:  # Откроем (создадим) итоговый файл с именем "filename".txt
        join_file.write(f'Даны файлы:\n')
        for file in create_file_list(folder):
            join_file.write(f'Назввание файла: {file[0]}\n')  # Записываем в итоговый файл имена начальных файлов
            join_file.write(f'Количество строк: {file[1]}\n')  # Записываем в итоговый файл число строк файлов
            for string in file[2]:
                join_file.write(string + '\n')  # Записываем в итоговый файл содержимое начальных файлов построчно
            join_file.write('\n')
    return print('Файл создан')


create_join_file('txt', 'join_file')

