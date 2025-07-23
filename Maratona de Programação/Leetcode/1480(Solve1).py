class Solution(object):
    def runningSum(self, nums):
        answer = []
        for i in range(0, len(nums)):
            sum = 0
            j = 0
            while j <= i:
                sum = sum + nums[j]
                j = j + 1
            answer.append(sum)
        return answer