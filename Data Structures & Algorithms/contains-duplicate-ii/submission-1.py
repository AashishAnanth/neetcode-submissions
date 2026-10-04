class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        key = {}
        for i in range(len(nums)):
            if nums[i] not in key:
                key[nums[i]] = i
            else:
                if abs(key[nums[i]] - i) <= k:
                    return True
                key[nums[i]] = i

        return False