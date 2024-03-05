class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        primes = [True] * n
        primes[0] = primes[1] = False
        sqrt_n = int(n ** 0.5) + 1

        for i in range(2, sqrt_n):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False

        return sum(primes)
