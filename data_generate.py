import random
from datetime import datetime, timedelta

def generate_random_date(start_year=2000, end_year=2024):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta_days = (end_date - start_date).days
    random_days = random.randint(0, delta_days)
    date = start_date + timedelta(days=random_days)
    return date.strftime("%d.%m.%Y")

def generate_random_dates(count=100, start_year=2000, end_year=2024):
    return [generate_random_date(start_year, end_year) for _ in range(count)]

def generate_partially_sorted_dates(count=100, disorder_fraction=0.1):
    dates = sorted(generate_random_dates(count))
    num_disorder = int(count * disorder_fraction)
    indices = random.sample(range(count), num_disorder)
    for i in indices:
        dates[i] = generate_random_date()
    return dates

def generate_partially_shuffled_dates(count=100, shuffle_fraction=0.1):
    dates = sorted(generate_random_dates(count))
    shuffle_size = max(1, int(count * shuffle_fraction))
    start = random.randint(0, count - shuffle_size)
    sublist = dates[start:start + shuffle_size]
    random.shuffle(sublist)
    dates[start:start + shuffle_size] = sublist
    return dates

def generate_unsorted_tail_dates(count=100, tail_fraction=0.2):
    sorted_part = sorted(generate_random_dates(int(count * (1 - tail_fraction))))
    tail_part = generate_random_dates(int(count * tail_fraction))
    return sorted_part + tail_part

def generate_reverse_sorted_dates(count=100):
    return sorted(generate_random_dates(count), reverse=True)

def save_dates_to_file(dates, filename="dates.txt"):
    with open(filename, 'w') as f:
        f.write(' '.join(dates))

def generate_date_array(filename="dates.txt", count=100, mode="random", **kwargs):
    """
    mode - тип массива:
        "random" - случайные даты,
        "partially_sorted" - частично отсортированные,
        "partially_shuffled" - частично перемешанные,
        "unsorted_tail" - неупорядоченный хвост,
        "reverse_sorted" - в обратном порядке
    """
    if mode == "random":
        array = generate_random_dates(count)
    elif mode == "partially_sorted":
        array = generate_partially_sorted_dates(count, kwargs.get("disorder_fraction", 0.1))
    elif mode == "partially_shuffled":
        array = generate_partially_shuffled_dates(count, kwargs.get("shuffle_fraction", 0.1))
    elif mode == "unsorted_tail":
        array = generate_unsorted_tail_dates(count, kwargs.get("tail_fraction", 0.2))
    elif mode == "reverse_sorted":
        array = generate_reverse_sorted_dates(count)
    else:
        raise ValueError(f"Unknown mode: {mode}")

    save_dates_to_file(array, filename)

if __name__ == "__main__":
    generate_date_array(filename="dates.txt", count=50000, mode="reverse_sorted", shuffle_fraction=0.15)
