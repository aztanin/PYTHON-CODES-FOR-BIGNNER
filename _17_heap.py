import heapq

age = [12,23,55,16,55,76,70,10]

print( heapq.nlargest(3,age) )
# [76, 70, 55]

print( heapq.nsmallest(3,age) )
# [10, 12, 16]

