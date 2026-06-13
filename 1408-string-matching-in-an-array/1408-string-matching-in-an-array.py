class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
         return [w for w in words if any(w != x and w in x for x in words)]
        