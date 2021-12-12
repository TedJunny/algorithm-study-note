class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        answer = []

        for i, j in zip(nums[:n], nums[n:]):
            answer += [i, j]

        return answer


solution = Solution()
print(solution.shuffle([1, 1, 2, 2], 2))
