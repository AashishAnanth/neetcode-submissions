class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2
            total = 0
            for p in piles:
                total += math.ceil(p / mid)
            
            if total > h:
                low = mid + 1
            else:
                high = mid - 1
        
        return low
