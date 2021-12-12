class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if coordinates[0] in "aecg":
            return coordinates[1] in "2468"
        else:
            return coordinates[1] in "1357"

        return sum(ord(i) for i in coordinates) % 2 == 1


solution = Solution()
print(solution.squareIsWhite("h3"))
