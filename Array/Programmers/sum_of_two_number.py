def solution(numbers):
    sums = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] not in sums:
                sums.append(numbers[i] + numbers[j])

    return sorted(sums)


print(solution([2, 1, 3, 4, 1]))
