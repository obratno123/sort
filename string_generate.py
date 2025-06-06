import random
import string

def generate_random_string(min_len=3, max_len=8):
    return ''.join(random.choices(string.ascii_lowercase, k=random.randint(min_len, max_len)))

def generate_random_strings(count=100, min_len=3, max_len=8):
    return [generate_random_string(min_len, max_len) for _ in range(count)]

def generate_partially_sorted_strings(count=100, disorder_fraction=0.1, min_len=3, max_len=8):
    arr = sorted(generate_random_strings(count, min_len, max_len))
    num_disorder = int(count * disorder_fraction)
    indices = random.sample(range(count), num_disorder)
    for i in indices:
        arr[i] = generate_random_string(min_len, max_len)
    return arr

def generate_partially_shuffled_strings(count=100, shuffle_fraction=0.1, min_len=3, max_len=8):
    arr = sorted(generate_random_strings(count, min_len, max_len))
    shuffle_size = max(1, int(count * shuffle_fraction))
    start = random.randint(0, count - shuffle_size)
    sublist = arr[start:start + shuffle_size]
    random.shuffle(sublist)
    arr[start:start + shuffle_size] = sublist
    return arr

def generate_unsorted_tail_strings(count=100, tail_fraction=0.2, min_len=3, max_len=8):
    sorted_part = sorted(generate_random_strings(int(count * (1 - tail_fraction)), min_len, max_len))
    tail_part = generate_random_strings(int(count * tail_fraction), min_len, max_len)
    return sorted_part + tail_part

def generate_reverse_sorted_strings(count=100, min_len=3, max_len=8):
    return sorted(generate_random_strings(count, min_len, max_len), reverse=True)

def save_strings_to_file(strings, filename="strings.txt"):
    with open(filename, 'w') as f:
        f.write(' '.join(strings))

def generate_string_array(filename="strings.txt", count=100, mode="random", min_len=3, max_len=8, **kwargs):
    """
    mode - тип массива:
        "random" - случайные строки,
        "partially_sorted" - частично отсортированные,
        "partially_shuffled" - частично перемешанные,
        "unsorted_tail" - неупорядоченный хвост,
        "reverse_sorted" - в обратном порядке
    """
    if mode == "random":
        array = generate_random_strings(count, min_len, max_len)
    elif mode == "partially_sorted":
        array = generate_partially_sorted_strings(count, kwargs.get("disorder_fraction", 0.1), min_len, max_len)
    elif mode == "partially_shuffled":
        array = generate_partially_shuffled_strings(count, kwargs.get("shuffle_fraction", 0.1), min_len, max_len)
    elif mode == "unsorted_tail":
        array = generate_unsorted_tail_strings(count, kwargs.get("tail_fraction", 0.2), min_len, max_len)
    elif mode == "reverse_sorted":
        array = generate_reverse_sorted_strings(count, min_len, max_len)
    else:
        raise ValueError(f"Unknown mode: {mode}")

    save_strings_to_file(array, filename)

if __name__ == "__main__":
    generate_string_array(filename="strings.txt", count=50000, mode="reverse_sorted", disorder_fraction=0.1)
