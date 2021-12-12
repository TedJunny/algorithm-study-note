class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
        return "[.]".join(address.split("."))


solution = Solution()
print(solution.defangIPaddr("1.1.1.1"))
