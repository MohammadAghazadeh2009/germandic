import csv
from word import Word

class WordsList():
    def __init__(self, filename="words-list.csv"):
        self.filename = filename
        self.words = []
        self.load_words()

    def add_word(self, word):
        self.words.append(word)
        self.save_word()
        print("New word is in your list now!!")