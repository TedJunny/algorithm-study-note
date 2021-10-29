def card_num(card_array, n, m):
    result = 0

    for i in range(n):
        min_value = min(card_array[i])
        result = max(result, min_value)

    return result


print(card_num([[7, 3, 1, 8], [3, 3, 3, 4]], 2, 4))
