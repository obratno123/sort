import random

def generate_random_array(size=100, min_val=0, max_val=1000):
    return [random.randint(min_val, max_val) for _ in range(size)]

def generate_partially_sorted_array(size=100, disorder_fraction=0.1):
    arr = list(range(size))
    num_disorder = int(size * disorder_fraction)
    indices = random.sample(range(size), num_disorder)
    for i in indices:
        arr[i] = random.randint(0, size)
    return arr

def generate_partially_shuffled_array(size=100, shuffle_fraction=0.1):
    arr = list(range(size))
    shuffle_size = int(size * shuffle_fraction)
    if shuffle_size == 0:
        shuffle_size = 1
    start = random.randint(0, size - shuffle_size)
    sublist = arr[start:start+shuffle_size]
    random.shuffle(sublist)
    arr[start:start+shuffle_size] = sublist
    return arr

def generate_array_with_unsorted_tail(size=100, tail_fraction=0.2, min_val=0, max_val=1000):
    sorted_part = list(range(int(size * (1 - tail_fraction))))
    tail_part = [random.randint(min_val, max_val) for _ in range(int(size * tail_fraction))]
    return sorted_part + tail_part

def generate_reverse_sorted_array(size=100):
    return list(range(size, 0, -1))

def generate_array(filename="arr.txt", size=100, min_val=0, max_val=9, mode="random", **kwargs):
    """
    mode - тип массива:
        "random" - случайный,
        "partially_sorted" - частично отсортированный (вставка),
        "partially_shuffled" - частично перемешанный,
        "unsorted_tail" - неупорядоченный хвост,
        "reverse_sorted" - отсортирован в обратном порядке
    kwargs - дополнительные параметры для конкретных функций (например, disorder_fraction)
    """
    if mode == "random":
        array = generate_random_array(size, min_val, max_val)
    elif mode == "partially_sorted":
        disorder_fraction = kwargs.get("disorder_fraction", 0.1)
        array = generate_partially_sorted_array(size, disorder_fraction)
    elif mode == "partially_shuffled":
        shuffle_fraction = kwargs.get("shuffle_fraction", 0.1)
        array = generate_partially_shuffled_array(size, shuffle_fraction)
    elif mode == "unsorted_tail":
        tail_fraction = kwargs.get("tail_fraction", 0.2)
        array = generate_array_with_unsorted_tail(size, tail_fraction, min_val, max_val)
    elif mode == "reverse_sorted":
        array = generate_reverse_sorted_array(size)
    else:
        raise ValueError(f"Unknown mode: {mode}")

    with open(filename, 'w') as f:
        f.write(' '.join(map(str, array)))

if __name__ == "__main__":
    generate_array(filename="arr.txt", size=250000, mode="random", disorder_fraction=0.1)
