class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        return [sum(nums[: i + 1]) for i in range(len(nums))]


solution = Solution()
print(solution.runningSum([1, 1, 1, 1, 1]))
