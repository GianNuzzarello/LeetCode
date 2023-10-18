"""
LeetCode: https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.


Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


"""

class Solution:

    def first_solution(self, s: str, t: str) -> bool:
        """
        Time: O(n log n) - because we are sorting the array in O(n log n)
        Space: O(1) - we are not using any extra space

        """

        return sorted(s) == sorted(t)
    
    def second_solution(self, s: str, t: str) -> bool:
        """
        Time: O(s+t) - we are iterating through boot of the strings once
        Space: O(s+t) - we use a set to store the elements

        """

        if len(s) != len(t):
            return False

        countS, countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c,0):
                return False

        return True
    
    def best_solution(self, s: str, t: str) -> bool:
        
        return self.first_solution(s, t)
    

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(Solution().first_solution(s, t))
    print(Solution().second_solution(s, t))
    print(Solution().best_solution(s, t))