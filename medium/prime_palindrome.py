class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x):
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False
            for i in range(3, int(x**0.5) + 1, 2):
                if x % i == 0:
                    return False
            return True

        def reverse(x):
            return int(str(x)[::-1])

        while True:
            if n == reverse(n) and is_prime(n):
                return n
            n += 1
            if 10**7 < n < 10**8:
                n = 10**8
