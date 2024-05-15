class TrieNode:
    def __init__(self):
        """
        Each TrieNode contains a dictionary of TrieNode children and possibly a value
        if the node corresponds to the end of a key.
        """
        self.val = None
        self.children = {}


class TrieMap:
    def __init__(self):
        """
        Initialize the TrieMap data structure.
        """
        self.root = TrieNode()
        self.size = 0
    
    def put(self, key, val):
        """
        Insert or update the given key-value pair in the TrieMap.
        If the key is new, increase the size of the TrieMap.
        :param key: String key to insert into the TrieMap
        :param val: Value associated with the key
        """
        node = self.root
        for c in key:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        if node.val is None:
            self.size += 1
        node.val = val

    def get_node(self, key):
        """
        get the last node of the path
        """
        node = self.root
        for c in key:
            node = node.children.get(c)
            if not node:
                return None
        return node
    
    def get(self, key):
        """
        Retrieve the value associated with the given key in the TrieMap.
        If the key does not exist, return None.
        :param key: String key to search for in the TrieMap
        :return: Value associated with the key, or None if the key does not exist
        """
        node = self.get_node(key)
        return node.val if node else None
    
    def remove_at_depth(self, node, key, depth):
        if not node:
            return None
        # remove the value at key
        if len(key) == depth: # reach to the end
            if node:
                node.val = None
                self.size -= 1
        else:
            c = key[depth]
            node.children[c] = self.remove_at_depth(node.children[c], key, depth + 1)

        # prune the trie (if no val and no children)
        if node.val is None and all(child is None for child in node.children.values()):
            return None
        return node

    def remove(self, key):
        """
        Remove the key and its associated value from the TrieMap, if it exists.
        If the key is found and removed, decrease the size of the TrieMap.
        :param key: String key to remove from the TrieMap
        """
        self.root = self.remove_at_depth(self.root, key, 0)

    def contains_key(self, key):
        """
        Check if the given key exists in the TrieMap.
        :param key: String key to check in the TrieMap
        :return: True if the key exists, False otherwise
        """
        node = self.get_node(key)
        return node and node.val is not None

    def has_key_with_prefix(self, prefix):
        """
        Check if there is at least one key that starts with the given prefix.
        :param prefix: String prefix to check for in the TrieMap
        :return: True if a key with the prefix exists, False otherwise
        """
        return bool(self.get_node(prefix))

    def shortest_prefix_of(self, query):
        """
        Find the shortest prefix of 'query' that is in the TrieMap.
        :param query: String to check for the shortest prefix in the TrieMap
        :return: The shortest prefix of 'query' that is a key in the TrieMap, or an empty string if no such prefix exists
        """
        node = self.root
        for idx, c in enumerate(query):
            node = node.children.get(c)
            if not node:
                break
            if node.val is not None: # is end
                return query[:idx + 1]
        return ""
        
    def longest_prefix_of(self, query):
        """
        Find the longest prefix of 'query' that is in the TrieMap.
        :param query: String to check for the longest prefix in the TrieMap
        :return: The longest prefix of 'query' that is a key in the TrieMap, or an empty string if no such prefix exists
        """
        node = self.root
        longest = ""
        for idx, c in enumerate(query):
            node = node.children.get(c)
            if not node:
                break
            if node.val is not None: # is end
                longest = query[:idx + 1]
        return longest


    def dfs(self, node, prefix, keys):
        if not node:
            return
        if node.val is not None: # reach to a key
            keys.append(prefix)
        for c in node.children:
            # Recursive call with extended prefix
            self.dfs(node.children[c], prefix + c, keys)  

    def keys_with_prefix(self, prefix):
        """
        Retrieve all keys in the TrieMap that start with the given prefix.
        :param prefix: String prefix to search keys for in the TrieMap
        :return: A list of keys that start with the prefix
        """
        keys = []
        node = self.get_node(prefix)
        self.dfs(node, prefix, keys)
        return keys
    

    def dfs_with_pattern(self, node, idx, pattern, path, keys):
        if not node:
            return
        # pattern has exhausted and found a key
        if idx == len(pattern) and node.val is not None: 
            keys.append(path)
            return
        if idx == len(pattern):
            return
        c = pattern[idx]
        if c == '.':
            # iterate all children
            for x in node.children:
                self.dfs_with_pattern(node.children[x], idx + 1, pattern,  path + x, keys)
        elif c in node.children:
            self.dfs_with_pattern(node.children[c], idx + 1, pattern, path + c, keys)
        

    def keys_with_pattern(self, pattern):
        """
        Find all keys in the TrieMap that match the given pattern. A dot (.) in the pattern can match any character.
        :param pattern: String pattern to match keys against, where '.' can match any character
        :return: A list of keys that match the pattern
        """
        keys = []
        self.dfs_with_pattern(self.root, 0, pattern, '', keys)
        return keys
    
    def has_key_with_pattern(self, pattern):
        """
        Check if there is at least one key in the TrieMap that matches the given pattern.
        :param pattern: String pattern to match keys against, where '.' can match any character
        :return: True if a matching key exists, False otherwise
        """
        return bool(self.keys_with_pattern(pattern))

    def get_size(self):
        """
        Get the number of key-value pairs present in the TrieMap.
        :return: The size of the TrieMap
        """
        return self.size