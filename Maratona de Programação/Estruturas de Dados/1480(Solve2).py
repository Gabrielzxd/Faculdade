class Solution(object):
    def runningSum(self, nums):
        runSum = [nums[0]]
        for i in range(1, len(nums)):
            runSum.append(runSum[i-1]+nums[i])
        return runSum