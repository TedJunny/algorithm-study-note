def to_one(n, k):
    count = 0

    while True:
        if n % k == 0:
            n /= k
        else:
            n -= 1
        count += 1

        if n == 1:
            break

    return count


print(to_one(9, 3))
