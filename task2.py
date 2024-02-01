'''
У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу
містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою.

Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл
та повертає список словників з інформацією про кожного кота.
'''

def get_cats_info(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            cats_info = []
            for line in lines:
                cat_data = line.strip().split(',')
                cat_info = {
                    'id': cat_data[0],
                    'name': cat_data[1],
                    'age': int(cat_data[2])
                }
                cats_info.append(cat_info)
            return cats_info
    except FileNotFoundError:
        print('Файл відсутній або пошкоджений')

cats_info = get_cats_info('task2_cats_info.txt')
print(cats_info)