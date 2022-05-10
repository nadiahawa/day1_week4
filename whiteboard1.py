#kristin
# Least Larger
# Given an array of numbers and an index, return the index of the least number
# larger than the element at the given index, or -1 if there is no such index.
# Example:
# Input: ([4, 1, 3, 5, 6], 0 ) 
# Output: 3
# Input: ([4, 1, 3, 5, 6], 4)
# Output: -1

def least_larger(nums, i):
    higher = [n for n in nums if n> nums[i]]
    if higher:
        return nums.index(min(higher))
    return -1


Write a function that takes in one argument (a_list), and reverses that list in-place.
l_1 = [10, 4, 3, 8, 4, 2, 6]
#need indexing and multiple variable assignemnt
def reverseInPlace(a_list):
    for i in range(len(a_list)//2):
        a_list[i], a_list[-(i+1)] = a_list[-(i+1)], a_list[i]

reverseInPlace(l_1)
print(l_1)


l_1 = [10, 4, 3, 8, 4, 2, 6]
def reverseInPlace(a_list):
     i = 0 # a pointer
     while i < len(a_list)//2:
         a_list[i], a_list[-(i+1)] = a_list[-(i+1)], a_list[i]
         i +=1

print(l_1)
reverseInPlace(l_1)
print(l_1