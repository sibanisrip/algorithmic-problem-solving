class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        result = []
        while num > 0:
            result.append(str(num % 7))
            num //= 7
        res = ''.join(result[::-1])

        return '-' + res if negative else res
        