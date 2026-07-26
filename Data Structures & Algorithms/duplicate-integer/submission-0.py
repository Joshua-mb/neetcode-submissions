class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        n=0
        while n < len(nums):
            if nums[n] in seen:
                return True
            seen.add(nums[n])
            n+=1
        return False