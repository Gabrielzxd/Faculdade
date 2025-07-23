class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        answer = []
        for i in nums:
            count = 0
            j = 0
            while j <= len(nums) - 1:
                if j == i:
                    j += 1
                if nums[j] < nums[i]:
                    count += 1
                j += 1
            answer.append(count)
        return answer