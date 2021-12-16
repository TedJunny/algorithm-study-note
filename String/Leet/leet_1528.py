class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        answer = [""] * len(s)

        for index, char in enumerate(s):
            answer[indices[index]] = char

        return "".join(answer)


solution = Solution()
print(solution.restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
