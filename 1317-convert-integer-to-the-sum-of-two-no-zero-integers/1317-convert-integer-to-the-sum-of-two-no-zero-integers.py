class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def hasZero(x):
            return '0' in str(x)
        for a in range(1,n):
            b=n-a
            if not hasZero(a) and not hasZero(b):
                return [a,b]       