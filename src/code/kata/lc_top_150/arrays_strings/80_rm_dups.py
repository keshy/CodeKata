"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # do one pass to mark anything that is repeating more than 2 times. You can get value of k here.
        # sort the array in place to get the updated list and return k and nums.
        dup_item = nums[0]
        dup_cnt = 0
        k = len(nums)
        for i, n in enumerate(nums):
            if dup_item == n:
                dup_cnt += 1
            else:
                dup_item = n
                dup_cnt = 1

            if dup_cnt > 2:
                nums[i] = 10001
                k -= 1

        list.sort(nums)
        print(nums)
        return k


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
    print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))
