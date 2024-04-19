"""
https://leetcode.com/problems/3sum/description/?envType=study-plan-v2&envId=top-interview-150
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        list.sort(nums)
        ref = {}
        for i, n in enumerate(nums):
            if ref.get(n):
                ref[n].append(i)
            else:
                ref[n] = [i]

        for i in range(0, len(nums)):
            p1 = i
            p2 = len(nums) - 1
            if nums[i] == nums[i - 1] and i > 0:
                continue
            while p1 < p2:
                # add p1 and p2
                t_sum = nums[p1] + nums[p2]
                # if sum is < 0 and dict look up is not returning anything - then move p1.
                mid_idxs = ref.get(-t_sum, -1)
                if mid_idxs != -1:
                    for id in mid_idxs:
                        if id > p1 and id < p2:
                            s = (nums[p1], nums[id], nums[p2])
                            result.add(s)
                if t_sum < nums[i]:
                    p1 += 1
                else:
                    p2 -= 1
        return [[x[0], x[1], x[2]] for x in result]


if __name__ == '__main__':
    c = Solution()
    print(c.threeSum([-1, 0, 1, 2, -1, -4]))
    print(c.threeSum([0, 0, 0]))
    print(c.threeSum([0, 1, 1]))
