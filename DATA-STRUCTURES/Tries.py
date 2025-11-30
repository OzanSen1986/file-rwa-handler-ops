class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"
    
    def add(self, word):
        current_level = self.root
        for c in word:
            if c not in current_level:
                current_level[c] = {}
            current_level = current_level[c]
        current_level[self.end_symbol] = True

    def search_level(self, current_level, current_prefix, words):
        if current_level is True:
            return words
        if self.end_symbol in current_level:
            words.append(current_prefix)
        for c in sorted(current_level.keys()):
            new_prefix = current_prefix + c
            words = self.search_level(current_level[c], new_prefix, words)
        return words

    def words_with_prefix(self, prefix):
        words = []
        current_level = self.root
        for c in prefix:
            if c not in current_level:
                return []
            current_level = current_level[c]
        words = []
        return self.search_level(current_level, prefix, words)
            

def main() -> None:
    obj_trie = Trie()
    obj_trie.add("developer")
    obj_trie.add("dev")
    obj_trie.add("manivela")
    print(obj_trie.root)

    
if __name__ == '__main__':
    main()
        










