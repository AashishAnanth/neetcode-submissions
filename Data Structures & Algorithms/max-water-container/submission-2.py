class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        best = 0

        while l < r:
            h = min(heights[l], heights[r])
            best = max(best, (r - l) * h)

            while l < r and heights[l] <= h:
                l += 1
            while l < r and heights[r] <= h:
                r -= 1
        
        return best