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
            total = 0
            for line in lines:
                numbers = re.findall(r'\d+', line)
                total += int(numbers[0])
            if len(lines) > 0:
                average = total / len(lines)
                return (total, average)
            else:
                return (0, 0)
    except FileNotFoundError:
        print('Файл відсутній або пошкоджений')

total, average = total_salary('task1_salary.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")