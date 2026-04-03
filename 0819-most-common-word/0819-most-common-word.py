class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        words=re.findall(r'\w+',paragraph)
        banned_set=set(banned)
        count=Counter(word for word in words if word not in banned_set)
        return count.most_common(1)[0][0]
        