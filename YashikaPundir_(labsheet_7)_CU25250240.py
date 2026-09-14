#1

"""class MaxHeap:
    def __init__(self):
        self.heap = []

    def heapify_up(self, i):
        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent] >= self.heap[i]:
                break

            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def heapify_down(self, i):
        n = len(self.heap)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left

            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == i:
                break

            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest

    def insert(self, x):
        self.heap.append(x)
        self.heapify_up(len(self.heap) - 1)

    def remove(self):
        if len(self.heap) == 0:
            return -1

        x = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        if len(self.heap) > 0:
            self.heapify_down(0)

        return x

    def display(self):
        for x in self.heap:
            print(x, end=" ")
        print()


class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify_up(self, i):
        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent] <= self.heap[i]:
                break

            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def heapify_down(self, i):
        n = len(self.heap)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def insert(self, x):
        self.heap.append(x)
        self.heapify_up(len(self.heap) - 1)

    def remove(self):
        if len(self.heap) == 0:
            return -1

        x = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        if len(self.heap) > 0:
            self.heapify_down(0)

        return x

    def display(self):
        for x in self.heap:
            print(x, end=" ")
        print()


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


maxHeap = MaxHeap()

maxHeap.insert(30)
maxHeap.insert(10)
maxHeap.insert(50)
maxHeap.insert(20)
maxHeap.insert(40)

print("Max Heap:", end=" ")
maxHeap.display()

print("Removed from Max Heap:", maxHeap.remove())

minHeap = MinHeap()

minHeap.insert(30)
minHeap.insert(10)
minHeap.insert(50)
minHeap.insert(20)
minHeap.insert(40)

print("Min Heap:", end=" ")
minHeap.display()

print("Removed from Min Heap:", minHeap.remove())

priorityQueue = MaxHeap()

priorityQueue.insert(5)
priorityQueue.insert(20)
priorityQueue.insert(10)
priorityQueue.insert(50)
priorityQueue.insert(30)

print("Priority Queue:", end=" ")
priorityQueue.display()

print("Highest Priority:", priorityQueue.remove())

arr = [40, 10, 30, 50, 20]

heap_sort(arr)

print("Heap Sort:", end=" ")
for i in arr:
    print(i, end=" ")

#2

n = int(input("Enter number of elements: "))

a = list(map(int, input("Enter array elements: ").split()))

a.sort()

ans = []

left = 0
right = n - 1

while left <= right:
    if left == right:
        ans.append(a[left])
        break

    ans.append(a[left])
    ans.append(a[right])

    left += 1
    right -= 1

total = 0

for i in range(n - 1):
    total += abs(ans[i] - ans[i + 1])

print("Rearranged Array:", end=" ")

for i in range(n):
    print(ans[i], end=" ")

print("\nTotal Sum =", total)"""

#3

n = int(input("Enter number of elements: "))

arr = list(map(int, input("Enter array elements: ").split()))

target = int(input("Enter target: "))

left = 0
minLength = n + 1
sum = 0

for right in range(n):
    sum += arr[right]

    while sum > target:
        minLength = min(minLength, right - left + 1)
        sum -= arr[left]
        left += 1

if minLength == n + 1:
    print("Output: -1")
else:
    print("Output:", minLength)