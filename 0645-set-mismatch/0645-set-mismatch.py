class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        dup = 0
        for x in nums:
            if x in s:
                dup = x
            s.add(x)

        for i in range(1, len(nums) + 1):
            if i not in s:
                return [dup, i]