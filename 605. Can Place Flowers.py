"""
605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 
Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted = 0
        if n == 0:
            return True

        # Check if you can plant at the beginning
        if len(flowerbed) >= 2 and flowerbed[0] == 0 and flowerbed[1] == 0:
            planted += 1
            flowerbed[0] = 1

        # Check if you can plant at the end
        if len(flowerbed) >= 2 and flowerbed[-1] == 0 and flowerbed[-2] == 0:
            planted += 1
            flowerbed[-1] = 1

        # Check if flowerbed is size 1
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            planted += 1
            flowerbed[0] = 1

        for plant in range(1, len(flowerbed)-1):
            if flowerbed[plant-1] == 0 and flowerbed[plant + 1] == 0:
                if flowerbed[plant] == 0:
                    planted += 1
                    flowerbed[plant] = 1
                    if planted == n:
                        return True

        return planted >= n