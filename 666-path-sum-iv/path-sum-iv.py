class Solution:
    def encode(self, depth: int, idx: int) -> int:
        return 10 * depth + idx

    def decode(self, code: int) ->  Tuple[int, int]:
        return divmod(code, 10)

    def pathSum(self, nums: List[int]) -> int:
        tree = {} # code: value
        s = 0

        for code in nums:
            code, value = divmod(code, 10)
            tree[code] = value


        root_code = nums[0] // 10

        def dfs(node_code, running_sum):
            nonlocal s
            if node_code not in tree:
                return
            
            value = tree[node_code]
            running_sum += value
            depth, idx = self.decode(node_code)

            left_code = self.encode(depth + 1, idx * 2 - 1)
            right_code = self.encode(depth + 1, idx * 2)

            if left_code not in tree and right_code not in tree:
                s += running_sum
                return
            dfs(left_code, running_sum)
            dfs(right_code, running_sum)

        dfs(root_code, 0)
        return s

        
        