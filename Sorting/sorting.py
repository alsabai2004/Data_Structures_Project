class Sorting:
    @staticmethod
    def bubble_sort(data):
        arr = data.copy()
        n = len(arr)

        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break

        return arr

    @staticmethod
    def selection_sort(data):
        arr = data.copy()

        for i in range(len(arr)):
            min_index = i

            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j

            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr

    @staticmethod
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

    @staticmethod
    def merge_sort(data):
        if len(data) <= 1:
            return data.copy()

        mid = len(data) // 2
        left = Sorting.merge_sort(data[:mid])
        right = Sorting.merge_sort(data[mid:])

        result = []
        i = j = 0

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

    @staticmethod
    def quick_sort(data):
        arr = data.copy()

        def quicksort(items, low, high):
            if low >= high:
                return

            pivot = items[high]
            i = low

            for j in range(low, high):
                if items[j] <= pivot:
                    items[i], items[j] = items[j], items[i]
                    i += 1

            items[i], items[high] = items[high], items[i]

            quicksort(items, low, i - 1)
            quicksort(items, i + 1, high)

        quicksort(arr, 0, len(arr) - 1)
        return arr

    @staticmethod
    def is_sorted(data):
        return all(data[i] <= data[i + 1] for i in range(len(data) - 1))
