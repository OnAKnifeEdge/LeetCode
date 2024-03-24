class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # if stickers are ["cat", "dog"]
        # [{"c": 1, "a": 1, "t: 1"}, {"d": 1, "o": 1, "g": 1}]
        # sticker_count = []
        # for i, s in enumerate(stickers):
        #     sticker_count.append({})
        #     for c in s:
        #         sticker_count[i][c] = 1 + sticker_count[i].get(c, 0)

        sticker_count = [Counter(sticker) for sticker in stickers]
        dp = {} # key = subseq of target, value = min num of stickers

        def dfs(t, sticker):
            if t in dp:
                return dp[t]
            result = 1 if sticker else 0
            remain_target = ""
            for c in t:
                if c in sticker and sticker[c] > 0:
                    sticker[c] -= 1
                else:
                    remain_target += c
            if remain_target: 
                used = float('inf')
                for sticker in sticker_count:
                    if remain_target[0] not in sticker:
                        continue
                    used = min(used, dfs(remain_target, sticker.copy()))
                dp[remain_target] = used
                result += used
            return result

        
        result = dfs(target, {})
        return result if result != float('inf') else -1