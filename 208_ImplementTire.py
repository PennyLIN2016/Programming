import collections
#Runtime: 192 ms, faster than 65.00% of Python online submissions for Implement Trie (Prefix Tree).
#Memory Usage: 38.6 MB, less than 41.76% of Python online submissions for Implement Trie (Prefix Tree).
class TrieNode(object):
    def __init__(self):
        self.Children=collections.defaultdict(TrieNode)
        self.WordFlag= False

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        tmp = self.root
        for value in word:
            tmp = tmp.Children[value]
        tmp.WordFlag= True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        tmp = self.root
        for value in word:
            tmp= tmp.Children.get(value)
            if tmp==None:
                return  False
        return tmp.WordFlag

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        tmp = self.root
        for value in prefix:
            tmp= tmp.Children.get(value)
            if tmp == None:
                return  False
        return True


