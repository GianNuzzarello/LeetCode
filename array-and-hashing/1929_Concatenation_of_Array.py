"""
LeetCode: https://leetcode.com/problems/concatenation-of-array/

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

 

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
 

Constraints:

n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 1000

"""

from typing import List

class Solution:

    def best_solution(self, nums: List[int]) -> List[int]:
        """
        Time: O(n) - The time complexity of list concatenation in Python is O(n), where n is 
        the total number of elements in both lists being concatenated.

        Space: O(n) - The space complexity is determined by the space required for the new list that is returned.
        In this case, the new list will contain all the elements of nums repeated twice. Therefore, the space complexity is O(2n), 
        which simplifies to O(n), where n is the length of the input list nums.

    
        """

        return nums + nums
    

if __name__ == "__main__":
    print(Solution().best_solution([1,3,2,1]))