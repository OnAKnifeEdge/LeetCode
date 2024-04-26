class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # 每个非空的二叉树节点都会产生两条边，并消耗一条边；而每个空节点只会消耗一条边
        edge = 1
        for val in preorder.split(","):
            edge -= 1
            if edge < 0:
                return False
            if val != "#":
                edge += 2

        return edge == 0
