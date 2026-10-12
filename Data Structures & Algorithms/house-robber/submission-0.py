class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, nums[0]
        for i in range(2, len(nums) + 1):
            a, b = b, max(b, a + nums[i-1])
        return b