import time
from sort import Sorter
from datetime import datetime

def read_array_from_file(filename="arr.txt"):
    with open(filename, "r") as f:
        return list(map(int, f.read().split()))

#def read_string_array_from_file(filename="strings.txt"):
    #with open(filename, "r") as f:
        #return f.read().split()
    
#def read_date_array_from_file(filename="dates.txt"):
    #with open(filename, "r") as f:
        #content = f.read().strip().split()
        #return [datetime.strptime(date_str, "%d.%m.%Y") for date_str in content]

def main():
    methods = [
        ("bubble", Sorter.bubble_sort),
        ("selection", Sorter.selection_sort),
        ("insertion", Sorter.insertion_sort),
        ("merge", Sorter.merge_sort),
        ("quick", Sorter.quick_sort),
        ("heap", Sorter.heap_sort),
        ("shell", Sorter.shell_sort),
        #("radix", Sorter.radix_sort),
        #("radix", Sorter.radix_sort_strings),
        ("python", Sorter.python_sort)
    ]

    array = read_array_from_file()
    #array = read_string_array_from_file()
    #array = read_date_array_from_file()

    print("Запуск всех сортировок...\n")
    for method_name, sort_func in methods:
        sorter = Sorter(array.copy())
        start_time = time.time()

        sort_func(sorter)
        end_time = time.time()
        elapsed = end_time - start_time

        print(f"{method_name.capitalize()} Sort:")
        print(f"Время: {elapsed:.6f} секунд\n")

        with open("random09.txt", "a") as f:
            f.write(f"{method_name} {len(array)} {elapsed:.6f}\n")

if __name__ == "__main__":
    main()
