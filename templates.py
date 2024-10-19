# Two Pointers
def two_pointers(nums):
    result = 0
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] == nums[right]:
            left += 1
        else:
            right -= 1
    return result

# Two pointers: two inputs, exhaust both
def two_pointers_2(nums1, nums2):
    result = 0
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            i += 1
        else:
            j += 1   
    while i < len(nums1):
        i += 1
    while j < len(nums2):
        j += 1
    return result

# sliding window
def sliding_window(nums):
    left = 0
    result = 0
    for right in range(len(nums)):
        while right > 0:
            left += 1    
    return result

# linkedlist: slow and fast pointer
def slow_and_fast():
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
# linkedlist: reverse
def reverse():
    pre, curr = None, head
    while curr:
        curr.next, pre, curr = pre, curr, curr.next
    return pre 

# monotonic stack: increasing
def monotonic_stack(nums):
    stack = []
    for num in nums:
        while stack and stack[-1] > num:
        # for monotonic decreasing, just flip the > to <
            stack.pop()
        stack.append(num)
        
def monotonic_queue(nums):
    pass
        
# binary tree
def dfs_binary_tree():
    if not root:
        return
    dfs_binary_tree(root.left)
    dfs_binary_tree(root.right)
    
def dfs_iterative():
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
            
def bfs_binary_tree():
    q = deque([root])
    while q:
        n = len(q)
        for _ in range(n):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
def dfs_graph(graph):
    visited = set()
    def dfs(node):
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor)
    dfs(root)
    
def dfs_graph_stack(graph):
    visited = {root}
    stack = [root]
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                
def bfs_graph(graph):
    q = deque([root])
    visited = {root}
    while q:
        n = len(q)
        for _ in range(n):
            node = q.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
    