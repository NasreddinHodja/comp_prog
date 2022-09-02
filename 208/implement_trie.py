#!/usr/bin/env python3

class TNode:
    def __init__(self, s="", is_word=False):
        self.s = s
        self.is_word = is_word
        self.children = [None] * 26

    def add_child(self, l):
        edge = ord(l) - ord("a")
        if self.children[edge] is None:
            self.children[edge] = TNode(self.s + l)
        # c = self.children[ord(l) - ord("a")]
        # if c is None: c = TNode(self.s + l)
        return self.children[edge]

    def __str__(self):
        s = f"s = {self.s}\n"
        s += f"children = {self.children}\n"
        return s


class Trie:

    def __init__(self):
        self.head = TNode()


    def insert(self, word: str) -> None:
        curr = self.head
        while curr is not None and word:
            curr = curr.add_child(word[0])
            word = word[1:]
            if not word:
                curr.is_word = True


    def search(self, word: str) -> bool:
        curr = self.head
        while word:
            edge = ord(word[0]) - ord("a")
            if curr.children[edge] is None:
                return False
            curr = curr.children[edge]
            word = word[1:]
        if curr.is_word:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        while prefix:
            edge = ord(prefix[0]) - ord("a")
            if curr.children[edge] is None:
                return False
            curr = curr.children[edge]
            prefix = prefix[1:]
        return True



# Your Trie object will be instantiated and called as such:
obj = Trie()

params = [
    obj.insert("apple"),
    obj.search("apple"),
    obj.search("app"),
    obj.startsWith("app"),
    obj.insert("app"),
    obj.search("app")
]
print(params)
