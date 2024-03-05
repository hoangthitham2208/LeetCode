class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_palindrome = lambda x: x == x[::-1]
        min_cuts = [i for i in range(n)]

        for i in range(1, n):
            for j in range(i + 1):
                if is_palindrome(s[j:i + 1]):
                    min_cuts[i] = min(min_cuts[i], 1 + min_cuts[j - 1] if j > 0 else 0)

        return min_cuts[-1]
