"""
0665. Non-decreasing Array
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
 

Constraints:

1 <= n <= 10 ^ 4
- 10 ^ 5 <= nums[i] <= 10 ^ 5
"""
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                cnt += 1
                if cnt > 1 or ((i - 1 >= 0 and nums[i - 1] > nums[i + 1]) and
                               (i + 2 < len(nums) and nums[i + 2] < nums[i])):
                    return False
        return True