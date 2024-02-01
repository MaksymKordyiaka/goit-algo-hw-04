'''
У вас є текстовий файл, який містить інформацію про місячні заробітні
плати розробників у вашій компанії. Кожен рядок у файлі містить прізвище
розробника та його заробітну плату, які розділені комою без пробілів.

Ваше завдання - розробити функцію total_salary(path), яка аналізує цей
файл і повертає загальну та середню суму заробітної плати всіх розробників.
'''
import re

def total_salary(path):
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            tot_salary = 0
            for line in lines:
                numbers = re.findall(r'\d+', line)
                tot_salary += int(numbers[0])
            if len(lines) > 0:
                average_salary = tot_salary / len(lines)
                return (tot_salary, average_salary)
            else:
                return (0, 0)
    except FileNotFoundError:
        print('Файл відсутній або пошкоджений')

result = total_salary('task1_salary.txt')
print(result)