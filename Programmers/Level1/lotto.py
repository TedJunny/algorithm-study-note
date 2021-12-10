def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    zero_count = lottos.count(0)
    hits = 0

    for lotto in lottos:
        if lotto in win_nums:
            hits += 1

    return [rank[zero_count + hits], rank[hits]]

    # answer = []
    # lotto_prize = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}
    # hits = 0

    # for lotto in lottos:
    #     if lotto in win_nums:
    #         hits += 1

    # zero_count = lottos.count(0)
    # best_hits = hits + zero_count

    # if hits == 0:
    #     hits = 1

    # if best_hits == 0:
    #     best_hits = 1

    # return [7 - best_hits, 7 - hits]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
