T = int(input())

for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    positive = False
    negative = False

    for x in A:
        if x > 0:
            positive = True
        elif x < 0:
            negative = True

    if positive and negative:
        print(-1)
    else:
        operations = 0

        for x in A:
            operations += abs(x)

        print(operations)