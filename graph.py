import matplotlib.pyplot as plt
from collections import defaultdict
import os

def find_file_in_subfolders(filename):
    for root, _, files in os.walk("."):
        if filename in files:
            return os.path.join(root, filename)
    raise FileNotFoundError(f"Файл '{filename}' не найден в текущей директории и подпапках.")

def plot_sorting_results(filename, save_plot):
    filepath = find_file_in_subfolders(filename)
    data = defaultdict(list)

    with open(filepath, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 3:
                method, size, time = parts
                data[method].append((int(size), float(time)))

    for method in data:
        data[method].sort()

    plt.figure(figsize=(12, 7))
    for method, results in data.items():
        sizes = [x[0] for x in results]
        times = [x[1] for x in results]
        plt.plot(sizes, times, marker='o', label=method.capitalize())

    plt.title("Сравнение алгоритмов сортировки")
    plt.xlabel("Размер массива")
    plt.ylabel("Время (секунды)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_plot)
    plt.show()
    print(f"График сохранён в файл: {save_plot}")

if __name__ == "__main__":
    plot_sorting_results("partially_sorted.txt", "partially_sorted.png")