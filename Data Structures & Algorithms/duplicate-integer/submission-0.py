class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        key = []
        for num in nums:
            if num not in key:
                key.append(num)
            else:
                return True
        return False