import os
import csv

current_directory = os.path.dirname(os.path.abspath(__file__))
files_directory = os.path.join(current_directory)

print('читаем файлы из', files_directory)
files_names = os.listdir(files_directory)
print('В директории найдены файлы:', *files_names)

# Шаблон заголовков для CSV-файла
headers_template = [
    'name',
    'surname',
    'age',
    'height',
    'weight',
    'eyesight',
    'education',
    'english_language'
]

# Путь к файлу для записи результата
result_file_path = os.path.join(current_directory, 'result.csv')
with open(
    result_file_path,
    mode='w',
    encoding='utf-8',
    newline=''
) as result_file:
    writer = csv.writer(result_file, delimiter='#')
    writer.writerow(['id'] + headers_template)

    sort_list = []

    # Перебор всех файлов в директории
    for file_name in files_names:
        file_path = os.path.join(files_directory, file_name)
        if not file_name.endswith('.csv'):
            continue
        with open(file_path, 'r', encoding='UTF-8') as file:
            reader = csv.reader(file, delimiter='#')
            headings = next(reader, None)
            if headings is None:
                print(f"Файл {file_name} не содержит данных.")
                continue

            # Проверка соответствия заголовков шаблону
            if not all(field in headings for field in headers_template):
                print(f'Файл {file_name} содержит неверные заголовки')
                continue

            # Фильтрация данных и добавление их в список sort_list
            for row in reader:
                age = int(row[headings.index('age')])
                eyesight = float(row[headings.index('eyesight')])
                weight = int(row[headings.index('weight')])
                education = str(row[headings.index('education')])
                english_language = str(row[headings.index('english_language')])
                height = int(row[headings.index('height')])
                if 20 <= age <= 59 and eyesight == 1.0 and 50 <= weight <= 90:
                    if education == 'Master' or education == 'PhD':
                        if english_language == 'true':
                            if height >= 150 and height <= 190:
                                name = row[headings.index('name')]
                                surname = row[headings.index('surname')]
                                sort_list.append([
                                    name,
                                    surname,
                                    age,
                                    height,
                                    weight,
                                    eyesight,
                                    education,
                                    english_language
                                ])

    # Сортировка данных по имени и фамилии
    sorted_data = sorted(sort_list, key=lambda x: (x[0], x[1]))

    # Запись отсортированных данных в CSV-файл
    for index, row in enumerate(sorted_data, start=1):
        writer.writerow([index] + row)
        print('#'.join([str(index)] + [str(item) for item in row[1:]]))
