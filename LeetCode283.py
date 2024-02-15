from typing import List


class Solution:
    def moveZeros(self, nums: List[int]) -> None:
        #Set a variable to point to the first position of all 0 elements in the array after
        # a series of operations.
        n = len(nums)
        #  using fast and slow pointer
        slow = 0
#     After traversal, slow points to an element that is 0
#     if there is no 0 in the array, it exceeds the range of the array, just as fast does
        for fast in range(n):
            #  slow should move to zeros
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        #  set all the elements after slow as zeros
        for i in range(slow,n):
            nums[i] = 0
        # do not return anything