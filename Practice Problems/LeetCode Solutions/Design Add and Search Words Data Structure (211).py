# This script creates a Trie data structure to solve LeetCode problem 211.
# From the question Descriptions...
# Design a data structure that supports adding new words and finding if a string matches any previously added string.
# Implement the WordDictionary class:
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
# Word may contain dots '.' where dots can be matched with any letter.


class TrieNode:
    # Trie node class to initialize the individual character nodes.
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}


class WordDictionary:
    # The actual Trie structure class is WordDictionary, initialize with a null root.
    def __init__(self):
        self.root = TrieNode('')

    # addword takes in a string, breakes the individual characters down into TrieNodes and their respective children, then find the ending character.
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True

    # dfs does a Depth First Search through each of the children of the given character's node.
    # If the index exceeds the length of the word we return the "is_end" property to see if complete.
    def dfs(self, index, node, word):
        if index >= len(word): return node.is_end

        current_char = word[index]
        # Check first in the normal case that we have an actual character.
        # If the node is logged move onto the specified child node.
        if current_char != '.':
            if current_char not in node.children:
                return False
            else:
                return self.dfs(index + 1, node.children[current_char], word)
        else:
            # If the character is a wild card we can check all the proceeding children nodes.
            if len(node.children) == 0:
                return False
            else:
                for i in node.children:
                    # If any of the children have a path to go through for dfs we return true.
                    if (self.dfs(index + 1, node.children[i], word)):
                        return True
    # search starts at index 0 of a word and initiates a DFS search to see if said word has already been catalogued.
    def search(self, word: str) -> bool:
        return self.dfs(0, self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
