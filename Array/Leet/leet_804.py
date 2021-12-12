class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_table = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]

        morse_codes = []

        for word in words:
            morse_codes.append("".join(morse_table[ord(letter) - ord("a")] for letter in word))

        return len(set(morse_codes))


solution = Solution()
print(solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
