class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def isprime(n):
            if n<=1:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True

        freq=Counter(nums)
        for count in freq.values():
            if isprime(count):
                return True
        return False
        