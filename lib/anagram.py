class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, matches):
        return [match for match in matches if set(match) == set(self.word)]