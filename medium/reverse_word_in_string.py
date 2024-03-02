class Solution:
    def reverseWords(self, s: str) -> str:
        list = s.split()
        reverse = []
        n = len(list)

        for i in range(n - 1, -1, -1):
            reverse.append(list[i])
        return " ".join(reverse)
