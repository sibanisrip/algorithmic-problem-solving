class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        t=0
        for i in range(0,len(nums),2):
            t+=nums[i]
        return t
        