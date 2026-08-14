class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l = 0
        seen = set()

        for r in range(1,len(nums)):
            if nums[r] == nums[r-1]:
                return True
            seen.add(r)
            
        return False
            