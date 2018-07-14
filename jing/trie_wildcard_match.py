from util.trie_node import TrieNode

def match(root, word):
    return _helper(root, word, 0)

def _helper(root, word, idx):
    if not root:
        return False
    if idx >= len(word):
        return root.is_word
    char = word[idx]
    if char != '*':
        return _helper(root.children.get(char), word, idx + 1)
    # deal with when current char is *
    no_char_match = _helper(root, word, idx + 1)
    if no_char_match:
        return True
    for dict_char, child in root.children.items():
        if _helper(child, word, idx):
            return True
    return False

root = TrieNode()
words = ["abc", "pad", "dad", "pxyzd", "pd", "ad", "cd"]
for word in words:
    TrieNode.add_word(root, word)

target = "*p*d*" # True
target2 = "p**d" # True
target3 = "xy"  # False
target4 = "a*c*" # True

print(match(root, target))