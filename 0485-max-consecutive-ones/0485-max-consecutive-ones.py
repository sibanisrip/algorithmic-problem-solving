class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        max_m=0
        for num in nums:
            if num==1:
                c+=1
                max_m=max(max_m,c)
            else:
                c=0
        return max_m
        