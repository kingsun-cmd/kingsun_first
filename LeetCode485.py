class Solution(object):
    def FindMaxConsevutiveOnes(self, nums):
        n = len(nums)
        lastZero = -1
        ans = 0
        # Access the array nums from left to right
        for i in range(n):
            # If the current element is 0, update lastZero
            if nums[i] == 0:
                lastZero = i
            else:
                # when the first element is 1, index is zero, so we need to minus lastZero
                ans = max(ans, i-lastZero)
        return ans