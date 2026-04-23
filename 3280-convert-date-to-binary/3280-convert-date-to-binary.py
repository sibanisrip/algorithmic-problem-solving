class Solution:
    def convertDateToBinary(self, date: str) -> str:
        part=date.split('-')
        res=[]
        for p in part:
            res.append(bin(int(p))[2:])
        return '-'.join(res)
        