class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        def getVal(c):
            if c == 'I':
                return 1
            elif c == 'V':
                return 5
            elif c == 'X':
                return 10
            elif c == 'L':
                return 50
            elif c == 'C':
                return 100
            elif c == 'D':
                return 500
            else:
                return 1000
        result=0
        for i in range(len(s)):
            curr=getVal(s[i])
            if i<len(s)-1:
                next_val=getVal(s[i+1])
                if curr<next_val:
                    result-=curr
                else:
                    result+=curr
            else:
                result+=curr
        return result
        