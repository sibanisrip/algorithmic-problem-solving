class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s_single=0
        s_double=0
        for num in nums:
            if num<10:
                s_single+=num
            else:
                s_double+=num
        return s_single!=s_double

        