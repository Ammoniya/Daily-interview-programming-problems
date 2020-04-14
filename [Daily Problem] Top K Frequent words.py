class Solution(object):
  def topKFrequent(self, words, k):
    data = dict()
    ans = list()
    for i in words:
        data[i]=0
    for i in words:
        data[i]+=1
    data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}    
    for i in data:
        if data[i] >= k:
            ans.append(i)     
    return ans        
words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']