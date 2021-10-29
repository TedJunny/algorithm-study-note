def big_num(data, n, m, k):
    result = 0

    data.sort()
    first_num = data[n - 1]
    second_num = data[n - 2]

    count = int(m / (k + 1) * k)
    count += m % (k + 1)  # 가장 큰 수가 더해지는 count에 대해서 연산

    result += count * first_num
    result += (m - count) * second_num
    return result


print(big_num([2, 4, 5, 4, 6], 5, 8, 3))
