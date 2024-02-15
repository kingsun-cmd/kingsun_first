from typing import List


class Solution:
    def removeDuplicates(selfs, nums: List[int]) -> int:
        n = len(nums)
        #  point j assign the position
        j = 0
        # traversal at point i
        for i in range(0,n):
            # if point i at the beginnig or the next point is the same as point i, then we skip
            if i == 0 or nums[i] != nums[i-1]:
                nums[j] = nums[i]
                # move j
                j += 1
        # return the number of unique elements
        return j
