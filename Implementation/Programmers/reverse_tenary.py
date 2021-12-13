def solution(n):
    rev_tenary = ""

    while n > 0:
        n, mod = divmod(n, 3)
        rev_tenary += str(mod)

    return int(rev_tenary, 3)


print(solution(45))
