#2523. Closest Prime Numbers in Range
# Input: left = 10, right = 19
# Output: [11,13]
# Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
# The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
# Since 11 is smaller than 17, we return the first pair.

import math
class Solution(object):
    def closestPrimes(self, left, right):
        MAX_LIMIT =10**6
        is_prime = [True] * (MAX_LIMIT + 1)
        is_prime[0]=is_prime[1]=False

        for i in range(2, int(math.sqrt(MAX_LIMIT)) + 1):
            if is_prime[i]:
                for j in range(i * i, MAX_LIMIT + 1, i):
                    is_prime[j] = False

        primes = [i for i in range(left, right + 1) if is_prime[i]]
        
        
        if len(primes) < 2:
            return [-1, -1]
        
        min_diff = float('inf')
        closest_pair = [-1, -1]

        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                closest_pair = [primes[i], primes[i + 1]]

        return closest_pair


        