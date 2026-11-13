import csv
from word import Word

class WordsList():
    def __init__(self, filename="words-list.csv"):
        self.filename = filename
        self.words = []
        self.load_words()