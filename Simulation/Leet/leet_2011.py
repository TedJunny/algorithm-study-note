class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        return sum("+" in s or -1 for s in operations)

        # answer = 0

        # for operation in operations:
        #     operation = operation.replace("X", "")

        #     if operation == "--":
        #         answer -= 1
        #     else:
        #         answer += 1

        # return answer


solution = Solution()
print(solution.finalValueAfterOperations(["--X", "++X", "X++"]))
