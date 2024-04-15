class Solution:
    # 定义：当运载能力为 x 时，需要 f(x) 天运完所有货物
    # f(x) 随着 x 的增加单调递减    
    def f(self, weights: List[int], x: int) -> int:
        days = 1  # Start counting from day 1
        cap = x    # Initial capacity for a day
        for w in weights:
            if cap < w:  # If the current package cannot fit in the remaining capacity
                cap = x  # Reset capacity for the new day
                days += 1  # Increment the days count
            cap -= w  # Ship the current package
        
        return days


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            # 需要让 f(x) 的返回值大一些, 收缩右侧边界
            if self.f(weights, mid) <= days:
                right = mid
            else:
                left = mid + 1
        return left
        

        