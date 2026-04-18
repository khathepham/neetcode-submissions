class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        
        i = 0
        j = len(nums) - 1
        A.sort()
        while True:
            total = A[i][0] + A[j][0]
            if total == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]
            if total > target:
                j -= 1
            if total < target:
                i += 1
            