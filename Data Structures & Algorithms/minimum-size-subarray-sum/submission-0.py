class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        curr = 0
        best = float('inf')

        for j in range(len(nums)):
            curr += nums[j]

            while curr >= target:
                best = min(best, j - i + 1)
                curr -= nums[i]
                i += 1

        return 0 if best == float('inf') else best