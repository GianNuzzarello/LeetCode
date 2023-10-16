"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109


"""
from typing import List

class Solution:


    def first_solution(self, nums: List[int]) -> bool:
        """
        Time: O(n log n) - because we are sorting the array in O(n log n)
        Space: O(1) - we are not using any extra space

        """

        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
            
        return False
            
    def second_solution(self, nums: List[int]) -> bool:
        """
        Time: O(n) - we are iterating through the array once
        Space: O(n) - we use a set to store the elements
        
        """

        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)

        return False
            
    
            

    def best_solution(self, nums: List[int]) -> bool:
        """
        Time: O(n) - we are iterating through the array once
        Space: O(n) - we use a set to store the elements

        """
        
        return len(nums) != len(set(nums))
    



if __name__ == "__main__":
    sol = Solution()
    print(sol.first_solution([1,2,3,1]))
    print(sol.second_solution([1,2,3,4]))
    print(sol.best_solution([1,1,1,3,3,4,3,2,4,2]))
    
