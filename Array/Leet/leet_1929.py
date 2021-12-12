class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums
        # return [nums[i] if i < len(nums) else nums[i - len(nums)] for i in range(2 * len(nums))]


solution = Solution()
print(solution.getConcatenation([1, 3, 2, 5]))
