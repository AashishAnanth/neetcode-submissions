class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        triangle = n*(n+1)/2

        return int(triangle - sum(nums))