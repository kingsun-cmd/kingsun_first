class Solution:
    '''
    same as LeetCode 26, except element instead of duplicates
    '''
    def removeElement(self, nums: List[int], val:int) -> int:
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j
