from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1
        counter = Counter(s)

        return all(counter[i] == counter[j] for i, j in zip(s[:-1], s[1:]))


solution = Solution()
print(solution.areOccurrencesEqual("abacbc"))
