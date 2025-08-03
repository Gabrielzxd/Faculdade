class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        answer = []
        for i in range(0, len(nums)):
            count = 0
            j = 0
            while j <= len(nums) - 1:
                if nums[j] < nums[i]:
                    count += 1
                j += 1
            answer.append(count)
        return answer