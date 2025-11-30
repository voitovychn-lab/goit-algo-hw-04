import random
import timeit


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


def measure(func, arr):
    return timeit.timeit(lambda: func(arr.copy()), number=1)


def generate_random(n):
    return [random.randint(0, 100000) for _ in range(n)]


def generate_sorted(n):
    return list(range(n))


def generate_reversed(n):
    return list(range(n, 0, -1))


sizes = [10, 100, 1000, 5000]

for n in sizes:
    print(f"\n--- N = {n} ---")
    datasets = {
        "Random": generate_random(n),
        "Sorted": generate_sorted(n),
        "Reversed": generate_reversed(n)
    }

    for dtype, data in datasets.items():
        print(f"\nDataset: {dtype}")
        print("Insertion:", measure(insertion_sort, data))
        print("Merge:", measure(merge_sort, data))
        print("Timsort:", measure(sorted, data))
