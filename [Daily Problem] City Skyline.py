def generate_skyline(buildings):
    MAX = max([i[1] for i in buildings])+1
    skyline = [0]*MAX
    data = []
    for i in buildings:
        for j in range(i[0]-1,i[1]):
            if skyline[j] < i[2]:
                skyline[j]=i[2]
                
    for x in range(len(skyline)-1):
        if skyline[x]!=skyline[x+1]:
            data.append((x+2,skyline[x+1]))   
    return data        
#            2 2 2
#            2 2 2
#        1 1 2 2 2 1 1
#        1 1 2 2 2 1 1
#        1 1 2 2 2 1 1
# pos: 1 2 3 4 5 6 7 8 9
print (generate_skyline([(2, 8, 3), (4, 6, 5)]))
# [(2, 3), (4, 5), (7, 3), (9, 0)]
