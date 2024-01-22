class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        res = [value for value in words1 if value in words2 and words1.count(value) == 1 and words2.count(value) == 1]
        return len(res)