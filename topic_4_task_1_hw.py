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
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def generate_data(n):
    return [random.randint(0, 100000) for _ in range(n)]


def measure_time(func, data):
    return timeit.timeit(lambda: func(data.copy()), number=1)


data = generate_data(5000)

t_insertion = measure_time(insertion_sort, data)
t_merge = measure_time(merge_sort, data)
t_timsort = measure_time(sorted, data)

print("Insertion Sort:", t_insertion)
print("Merge Sort:", t_merge)
print("Timsort (sorted):", t_timsort)
