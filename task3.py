'''
Розробіть скрипт, який приймає шлях до директорії в якості аргументу
командного рядка і візуалізує структуру цієї директорії, виводячи імена
всіх піддиректорій та файлів. Для кращого візуального сприйняття,
імена директорій та файлів мають відрізнятися за кольором.
'''

from pathlib import Path
from colorama import Fore, Style
import sys

def list_files_and_directories(directory_path):
    try:
        path = Path(directory_path)
        for entry in path.iterdir():
            if entry.is_dir():
                print(Fore.BLUE + f"Директорія: {entry.name}")
                list_files_and_directories(entry)
            elif entry.is_file():
                print(Fore.GREEN + f"Файл: {entry.name}")
    except FileNotFoundError:
        print(f"Директорія не знайдена: {directory_path}")
    except PermissionError:
        print(f"Дозвіл відмовлено для директорії: {directory_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
    else:
        directory_path = sys.argv[1]
        if Path(directory_path).exists() and Path(directory_path).is_dir():
            list_files_and_directories(directory_path)
        else:
            print(f"Invalid directory path: {directory_path}")