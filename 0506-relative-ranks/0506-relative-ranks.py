class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = {x: i + 1 for i, x in enumerate(sorted(score, reverse=True))}
        ans = []

        for s in score:
            if rank[s] == 1:
                ans.append("Gold Medal")
            elif rank[s] == 2:
                ans.append("Silver Medal")
            elif rank[s] == 3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(rank[s]))

        return ans