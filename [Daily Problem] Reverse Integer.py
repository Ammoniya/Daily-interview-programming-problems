def reverse_integer(num):
    ans = 0
    if '-' == str(num)[0]:
        num = list(str(num))[1:]
        LEN = len(num)
        for i in range(LEN):
            ans+=(int(num[i])*(10**i))
        return ans
    else:
        num = list(str(num))
        LEN = len(num)
        for i in range(LEN):
            ans+=(int(num[i])*(10**i))
        return ans
print(reverse_integer(135))
# 531

print(reverse_integer(-321))
# -123
