class Solution:
  def buddyStrings(self, A, B):
    LEN = len(A)
    for i in range(LEN-1):
        for j in range(i+1,LEN):
            x=list(A)
            x[i],x[j]=x[j],x[i]
            if B == ''.join(x):
                return True
    return False

print (Solution().buddyStrings('ab', 'ba'))
print (Solution().buddyStrings('ab', 'ab'))
print (Solution().buddyStrings('aa', 'aa'))
print (Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
print (Solution().buddyStrings('', 'aa'))


print (Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print (Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False