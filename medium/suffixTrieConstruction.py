class SuffixTrie:
    """
    root : dict
    """

    def __init__(self, string=""):
        self.root = dict()
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        if string is None:
            self.root = {self.endSymbol: True}
            return

        for index in range(len(string)):
            self.addSuffixies(string, index)

    def addSuffixies(self, string, start_index):
        dictionary = self.root
        for index in range(start_index, len(string)):
            if string[index] not in dictionary:
                dictionary[string[index]] = {}
            dictionary = dictionary[string[index]]

        dictionary[self.endSymbol] = True

    def contains(self, string):
        dictionary = self.root
        for char in string:
            if char not in dictionary:
                return False
            dictionary = dictionary[char]

        return self.endSymbol in dictionary


def main():
    string = "dexterity"

    trie = SuffixTrie()
    trie.populateSuffixTrieFrom(string)
    print(trie.contains("abc"))
    print(trie.contains("dexter"))
    print(trie.contains("ty"))
    print(trie.contains("erity"))
    print(trie.contains(""))


if __name__ == "__main__":
    main()
