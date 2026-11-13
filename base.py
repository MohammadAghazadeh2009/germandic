import csv
from word import Word

class WordsList():
    def __init__(self, filename="words-list.csv"):
        self.filename = filename
        self.words = []
        self.load_words()

    def add_word(self, word):
        self.words.append(word)
        self.save_words()
        print("New word is in your list now!!")

    def remove_word(self, word):
        for w in self.words:
            if w.word == word:
                self.words.remove(w)
                self.save_words()
                print("Word deleted")
                return
        print("Word not found")
