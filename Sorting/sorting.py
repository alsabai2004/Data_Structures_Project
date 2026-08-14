def bubble_sort(data):
    arr = data.copy()

    for i in range(len(arr)):
        swapped = False

        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


def selection_sort(data):
    arr = data.copy()

    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[i], arr[minimum] = arr[minimum], arr[i]

    return arr


def insertion_sort(data):
    arr = data.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge_sort(data):
    if len(data) <= 1:
        return data.copy()

    middle = len(data) // 2

    left = merge_sort(data[:middle])
    right = merge_sort(data[middle:])

    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def quick_sort(data):
    if len(data) <= 1:
        return data.copy()

    pivot = data[len(data) // 2]

    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
