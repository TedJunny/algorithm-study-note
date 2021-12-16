class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for _ in range(10)]

        for i in range(0, len(rings), 2):
            rods[int(rings[i + 1])].add(rings[i])

        return sum(len(rod) == 3 for rod in rods)

        rods = [""] * 10

        for idx in range(len(rings) // 2):
            rods[int(rings[2 * idx + 1])] += rings[2 * idx]

        return sum("R" in rod and "G" in rod and "B" in rod for rod in rods)


solution = Solution()
print(solution.countPoints("B0B6G0R6R0R6G9"))
