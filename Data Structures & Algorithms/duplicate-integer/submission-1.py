class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        return not len(set_nums) == len(nums)