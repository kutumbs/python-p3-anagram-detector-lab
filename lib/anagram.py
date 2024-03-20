# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        self.word_list = word_list

        return [element for element in self.word_list if sorted(self.word) == sorted(element) ]