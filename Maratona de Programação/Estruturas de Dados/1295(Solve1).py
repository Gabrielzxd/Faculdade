class Solution(object):
    def findNumbers(self, nums):
        i = 0
        while i < len(nums):
            aux = nums[i]
            j = 0
            while(aux != 0):
                j = j + 1
                aux = aux // 10
            if(j % 2 != 0):
                nums.pop(i)
            else:
                i = i + 1
        return len(nums)
    

# Complexity O(N.M)