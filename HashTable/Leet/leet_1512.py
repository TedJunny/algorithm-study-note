class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        hash_map = {}
        res = 0
        for number in nums:
            if number in hash_map:
                res += hash_map[number]
                hash_map[number] += 1
            else:
                hash_map[number] = 1
        return res

        pairs = []
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1

        return count


solution = Solution()
print(solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
