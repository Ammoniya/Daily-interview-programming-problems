def square_sum(n):
    if n<=3:
        return n
    Ans = n    
    for i in range(1,n+1):
        COUNT = i*i
        if n < COUNT:break
        else:Ans = min(Ans,square_sum(n-COUNT)+1)
    return Ans
    
print(square_sum(13))
# Min sum is 32 + 22
# 2
