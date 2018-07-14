class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    @staticmethod
    def add_word(root, word):
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
        root.is_word = True

    @staticmethod
    def has_word(root, word):
        for char in word:
            root = root.children.get(char)
            if not root:
                return False
        return root.is_word