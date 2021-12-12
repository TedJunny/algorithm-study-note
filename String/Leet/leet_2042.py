import re


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        numbers = re.findall("\d+", s)
        return numbers == sorted(set(numbers), key=int)
        numbers = list(map(int, numbers))

        return all(i < j for i, j in zip(numbers[:-1], numbers[1:]))


solution = Solution()
print(solution.areNumbersAscending("hello world 1, 2 x 5"))
