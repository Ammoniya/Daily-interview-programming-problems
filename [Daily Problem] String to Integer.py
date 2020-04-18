def convert_to_int(s):
    if s[0]=='-':
        LEN = len(s)-1
        ans = 0
        s = s[1:]
        for i in range(0,LEN):
            ans+=((ord(s[i])-ord('0'))*(-10**(LEN-i-1)))
        return ans    
    else:
        LEN = len(s)
        ans = 0
        for i in range(0,LEN):
            ans+=((ord(s[i])-ord('0'))*(10**(LEN-i-1)))
        return ans 
  

print(convert_to_int('-105') + 1)
# -104
print(convert_to_int('105') + 1)
# -106