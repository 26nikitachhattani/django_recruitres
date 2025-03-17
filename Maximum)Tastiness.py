#Maximum Tastiness of Candy Basket
# Input: price = [13,5,1,8,21,2], k = 3
# Output: 8
# Explanation: Choose the candies with the prices [13,5,21].
# The tastiness of the candy basket is: min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8.
# It can be proven that 8 is the maximum tastiness that can be achieved.
class Solution(object):
    def maximumTastiness(self, price, k):
        price.sort()
        
        def is_valid(t):
            count = 1
            prev = price[0]
            for i in range(1, len(price)):
                if price[i] - prev >= t:
                    count += 1
                    prev = price[i]
                    if count == k:
                        return True
            return False
        
        left, right = 0, price[-1] - price[0]
        best = 0
        
        while left <= right:
            mid = (left + right) // 2
            if is_valid(mid):
                best = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return best
