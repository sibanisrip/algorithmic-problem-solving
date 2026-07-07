class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans=[]
        num=0
        for bit in nums:
            num=(num*2+bit)%5
            ans.append(num==0)
        return ans
