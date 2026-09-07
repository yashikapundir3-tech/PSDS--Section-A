#1 3 SUM PROBLEM 
arr = [-3, 1, 2, 5, 6, -3, 8, 1, 9, 2]

n = len(arr)

arr.sort()

print("Triplets with sum 0:")

for i in range(n - 2):

    if i > 0 and arr[i] == arr[i - 1]:
        continue

    left = i + 1
    right = n - 1

    while left < right:

        sum = arr[i] + arr[left] + arr[right]

        if sum == 0:
            print(arr[i], arr[left], arr[right])

            while left < right and arr[left] == arr[left + 1]:
                left += 1

            while left < right and arr[right] == arr[right - 1]:
                right -= 1

            left += 1
            right -= 1

        elif sum < 0:
            left += 1

        else:
            right -= 1

#2 FIBONACCI SERIES
n = int(input("Enter number of terms: "))

a = 1
b = 1

print("Fibonacci Series:", end=" ")

for i in range(1, n + 1):
    print(a, end=" ")

    c = a + b
    a = b
    b = c

#3 TOWER OF HANOI
def tower_of_hanoi(n, source, auxiliary, destination):

    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    print("Move disk", n, "from", source, "to", destination)

    tower_of_hanoi(n - 1, auxiliary, source, destination)


n = int(input("Enter number of disks: "))

tower_of_hanoi(n, 'A', 'B', 'C')
