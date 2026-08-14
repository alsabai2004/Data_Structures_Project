class Searching:
    @staticmethod
    def binary_search(data, target):
        low = 0
        high = len(data) - 1

        while low <= high:
            mid = (low + high) // 2

            if data[mid] == target:
                return mid

            if data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1
