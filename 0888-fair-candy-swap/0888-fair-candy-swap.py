class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(bobSizes) - sum(aliceSizes)) // 2
        s = set(bobSizes)

        for x in aliceSizes:
            if x + diff in s:
                return [x, x + diff]