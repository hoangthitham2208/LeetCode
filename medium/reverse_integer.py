class Solution:
    def reverse(self, x: int) -> int:
        if (x < 0):
            signed = -1
        else:
            signed = 1

        reversed = 0
        y = abs(x)
        while (y):
            digit = y % 10
            y = y // 10
            reversed = reversed * 10 + digit

        if (reversed > 2 ** 31 - 1) or reversed < (-2 ** 31 - 1):
            return 0
        else:
            return signed * reversed



