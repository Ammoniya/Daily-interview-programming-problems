class Solution(object):
  def findAllConcatenatedWordsInADict(self, words):
    LEN = len(words)
    for i in range(LEN-1):
        for j in range(i+1,LEN):
            if words[i]+words[j] in words: yield words[i]+words[j]
            if words[j]+words[i] in words: yield words[j]+words[i]
                
    
input = ["tech", "lead", "techlead", "cat", "cats", "dog", "catsdog"]

print(list(Solution().findAllConcatenatedWordsInADict(input)))