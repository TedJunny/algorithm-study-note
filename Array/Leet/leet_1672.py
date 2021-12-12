class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(map(sum, accounts))
        return max(sum(i) for i in accounts)


solution = Solution()
print(solution.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
