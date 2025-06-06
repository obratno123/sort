from collections import defaultdict
import pandas as pd
import os

def find_file_in_subfolders(filename):
    for root, _, files in os.walk("."):
        if filename in files:
            return os.path.join(root, filename)
    raise FileNotFoundError(f"Файл '{filename}' не найден в текущей директории и подпапках.")

def display_results(filename, excel_filename):
    filepath = find_file_in_subfolders(filename)
    results = defaultdict(dict)

    with open(filepath, "r") as file:
        for line in file:
            method, size, time = line.strip().split()
            size = int(size)
            time = float(time)
            results[size][method.capitalize()] = time

    df = pd.DataFrame.from_dict(results, orient='index')
    df.index.name = 'Размер'
    df = df.sort_index()

    df.to_excel(excel_filename, float_format="%.6f")
    print(f"Таблица успешно сохранена в файл: {excel_filename}")

if __name__ == "__main__":
    display_results("partially_sorted.txt", "partially_sorted.xlsx")