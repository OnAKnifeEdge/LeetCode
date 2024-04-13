class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        nums = [0] * len(s)
        mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        for i, c in enumerate(s):
            nums[i] = mapping[c]
        seen = set()
        result = set()

        L = 10 # 位数
        R = 4 # 进制
        # 存储 R^(L - 1) 的结果
        C = R ** (L - 1)

        window_hash = 0 # 维护滑动窗口中字符串的哈希值

        left, right = 0, 0
        while right < len(s):
            # 扩大窗口，移入字符，并维护窗口哈希值（在最低位添加数字）
            window_hash = R * window_hash + nums[right]
            right += 1

            if right - left == L:
                if window_hash in seen:
                    result.add(s[left:right])
                else:
                    seen.add(window_hash)
                window_hash -= nums[left] * C
                left += 1
        return list(result)