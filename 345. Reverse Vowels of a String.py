"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"
 
Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters."""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        str_list = list(s)
        stack = []
        for char in s:
            if char in vowels:
                stack.append(char)
        if len(stack) <= 1:
            return s
        else:
            for index, char in enumerate(s):
                if char in vowels:
                    str_list[index] = stack.pop()
            return "".join(str_list)

