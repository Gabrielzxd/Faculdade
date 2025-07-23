def smallerNumbersThanCurrent(nums):
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


nums = [8,1,2,2,3]
answer = smallerNumbersThanCurrent(nums)
print(answer)