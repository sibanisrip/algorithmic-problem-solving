class Solution:
    def canAliceWin(self, n: int) -> bool:
        pile=n
        stones_removed=10
        alice=True
        while pile >=stones_removed:
            pile=pile-stones_removed
            stones_removed -= 1 
            alice= not alice
        return not alice


        