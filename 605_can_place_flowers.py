# https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        l = len(flowerbed)

        for i in range(l):
            # 现在的花盆是空的
            # 前一个花盆也是空的或者是第一个
            # 后一个花盆也是空的或者是最后一个

            if flowerbed[i] == 0 \
                    and (i == 0 or flowerbed[i - 1] == 0) \
                    and (i == l - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n = n - 1
                if n == 0:
                    return True
        return False
