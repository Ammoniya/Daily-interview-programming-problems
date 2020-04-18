def square_numbers(nums):
    return list(sorted(map(lambda x:x*x,nums)))
    
print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
# [0, 1, 1, 9, 16, 25, 25]
