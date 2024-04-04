class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        # 如果开口朝上，越靠近对称轴函数值越小
        # 如果开口朝下，越靠近对称轴函数值越大

        l = len(nums)
        i, j = 0, l - 1
        result = [0] * l
        p = l - 1 if a > 0 else 0
        while i <= j:
            v1 = self.f(nums[i], a, b, c)
            v2 = self.f(nums[j], a, b, c)
            if a > 0: # 开口朝上
                if v1 >= v2:
                    result[p] = v1
                    i += 1
                else:
                    result[p] = v2
                    j -= 1
                p -= 1
            else: # 开口朝下
                if v1 <= v2:
                    result[p] = v1
                    i += 1
                else:
                    result[p] = v2
                    j -= 1
                p += 1
        return result



    def f(self, x: int, a: int, b: int, c: int) -> int:
        return a * x ** 2 + b * x + c
        