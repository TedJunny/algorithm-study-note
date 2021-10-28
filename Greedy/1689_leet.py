class Solution:
    def minPartitions(self, n: str) -> int:
        new_list = []

        for i in range(len(n)):
            new_list.append(int(n[i]))

        return max(new_list)
