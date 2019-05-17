# solution 1:
#Runtime: 128 ms, faster than 93.12% of Python online submissions for Add and Search Word - Data structure design.
#Memory Usage: 22.4 MB, less than 94.38% of Python online submissions for Add and Search Word - Data structure design.
import collections
class WordDictionary1(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = collections.defaultdict(list)


    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        if not word:
            return
        self.root[len(word)].append(word)



    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        if "." not in word:
            return  word in self.root[len(word)]
        for value in self.root[len(word)]:
            flag= 0
            for i in range(len(word)):
                if word[i]!= value[i] and word[i]!='.':
                    flag = 1
                    break
            if flag == 0 : return True
        return False

# solution 2: define the tier node
#Runtime: 428 ms, faster than 32.26% of Python online submissions for Add and Search Word - Data structure design.
#Memory Usage: 36.1 MB, less than 28.34% of Python online submissions for Add and Search Word - Data structure design.
import collections
class Node(object):
    def __init__(self):
        self.IsWord = False
        self.children = collections.defaultdict(list)
class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        tmp = self.root
        for value in word:
            if value not in tmp.children:
                tmp.children[value]=Node()
            tmp = tmp.children[value]
        tmp.IsWord = True


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could              contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        stack = [[self.root ,word]]
        #print(self.root.children)
        while stack:
            node,w = stack.pop()
            if not w:
                if node.IsWord:
                    return  True
            elif w[0]=='.':
                for c in node.children.values():
                    stack.append([c,w[1:]])
            elif w[0] in node.children:
                stack.append([node.children[w[0]],w[1:]])
        return False

obj = WordDictionary()
obj.addWord('word')
param_2 = obj.search('word')
print(param_2)

