class Sorter:
    def __init__(self, array):
        self.array = array
        
    def print_array(self):
        print("Sorted array:", self.array)

    def bubble_sort(self):
        arr = self.array
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    def selection_sort(self):
        arr = self.array
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    def insertion_sort(self):
        arr = self.array
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def merge_sort(self):
        self.array = self._merge_sort(self.array)

    def _merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self._merge_sort(arr[:mid])
        right = self._merge_sort(arr[mid:])
        return self._merge(left, right)

    def _merge(self, left, right):
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

    def quick_sort(self):
        self.array = self._quick_sort(self.array)

    def _quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self._quick_sort(left) + middle + self._quick_sort(right)

    def heap_sort(self):
        arr = self.array
        n = len(arr)

        def heapify(n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[l] > arr[largest]:
                largest = l
            if r < n and arr[r] > arr[largest]:
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(n, largest)

        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(i, 0)

    def shell_sort(self):
        arr = self.array
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2

    def radix_sort(self):
        arr = self.array
        if len(arr) == 0:
            return
        max_num = max(arr)
        exp = 1
        while max_num // exp > 0:
            self._counting_sort(exp)
            exp *= 10

    def _counting_sort(self, exp):
        n = len(self.array)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = self.array[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            index = self.array[i] // exp
            output[count[index % 10] - 1] = self.array[i]
            count[index % 10] -= 1

        for i in range(n):
            self.array[i] = output[i]
    def radix_sort_strings(self):
        arr = self.array
        if len(arr) == 0:
            return
        
        max_len = max(len(s) for s in arr)

        for pos in reversed(range(max_len)):
            self._counting_sort_strings(pos)

    def _counting_sort_strings(self, pos):
        n = len(self.array)
        output = ["" for _ in range(n)]
        count = [0] * 257 

        for s in self.array:
            index = ord(s[pos]) if pos < len(s) else 0
            count[index + 1] += 1 

        for i in range(1, 257):
            count[i] += count[i - 1]

        for s in self.array:
            index = ord(s[pos]) if pos < len(s) else 0
            output[count[index]] = s
            count[index] += 1

        self.array = output

    def python_sort(self):
        self.array.sort()