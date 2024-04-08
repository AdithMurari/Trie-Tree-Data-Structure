class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

class SpellChecker:
    def __init__(self, dictionary):
        self.trie = Trie()
        self.load_dictionary(dictionary)

    def load_dictionary(self, dictionary):
        for word in dictionary:
            self.trie.insert(word.lower())

    def check_spelling(self, word):
        return self.trie.search(word.lower())

    def spell_check_document(self, document):
        misspelled_words_per_line = []
        lines = document.split('\n')

        for line_number, line in enumerate(lines, start=1):
            misspelled_words = []
            words = line.split()

            for word in words:
                word = word.strip('.,!?()[]{}"\':;')

                if not self.check_spelling(word):
                    misspelled_words.append(word)

            if misspelled_words:
                misspelled_words_per_line.append((line_number, misspelled_words))

        return misspelled_words_per_line


class FileLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_file_lines(self):
        try:
            with open(self.file_path, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"File not found: {self.file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
        return []


if __name__ == "__main__":
    words_file_path = input("Enter the file name containing all the words: ").strip()
    document_file_path = input("Enter the file name for checking misspelled words: ").strip()

    words_loader = FileLoader(words_file_path)
    document_loader = FileLoader(document_file_path)

    dictionary_words = words_loader.load_file_lines()
    dictionary_words = [word.strip().lower() for word in dictionary_words]

    if dictionary_words:
        spell_checker = SpellChecker(dictionary_words)
        document_lines = document_loader.load_file_lines()
        for line_number, line in enumerate(document_lines, start=1):
            misspelled_words = spell_checker.spell_check_document(line)

            if misspelled_words:
                for line_number_misspelled, misspelled_words_list in misspelled_words:
                    if misspelled_words_list:
                        print(f"Line {line_number} - Misspelled words: {', '.join(misspelled_words_list)}")
                    else:
                        print(f"Line {line_number} - No misspelled words.")
                continue

            print(f"Line {line_number} - No misspelled words.")



