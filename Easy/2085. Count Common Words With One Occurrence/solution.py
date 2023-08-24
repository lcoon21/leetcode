class Solution:
    
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        res = 0
        for elem in words1:
            if words1.count(elem) == 1 and elem in words2 and words2.count(elem) == 1:
                res += 1
            # else:
            #     words1 = list(filter((elem).__ne__, words1))

        return(res)

# cmd shift f