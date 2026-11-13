class Word():
    def __init__(self, word, meaning, example, level):
        self.word = word
        self.meaning = meaning
        self.example = example
        self.level = level

    def to_list(self):
        return [self.word, self.meaning, self.example, self.level]

    def from_list(data):
        return Word(data[0], data[1], data[2], data[3])