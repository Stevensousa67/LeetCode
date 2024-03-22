"""
169. Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    
        # My initial solution
        hash_map = {}

        for num in nums:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        
        for num in nums:
            if hash_map[num] > len(nums) / 2:
                return num
            
        # My second solution (when I couldn't remember how to use dictionaries)
        # count = 1
        # fast_pointer, slow_pointer = 1, 0
        # nums.sort()

        # while fast_pointer < len(nums):
        #     if nums[fast_pointer] == nums[slow_pointer]:
        #         count += 1
        #         if count > len(nums) // 2:
        #             slow_pointer += 1
        #             break
        #     else:
        #         count = 1
        #         slow_pointer = fast_pointer
        #     fast_pointer += 1
        # return nums[slow_pointer]