class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        hash_map = {}

        for idx, num in enumerate(sorted(nums)):
            hash_map.setdefault(num, idx)

        return [hash_map[num] for num in nums]


solution = Solution()
print(solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
