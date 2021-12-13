from collections import Counter


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]


print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
