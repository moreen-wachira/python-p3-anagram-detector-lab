class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        result = []

        # Iterate through each word in the word_list
        for candidate in word_list:
            # Check if the candidate is not the same as the initialized word
            # and if it is an anagram
            if candidate.lower() != self.word.lower() and self.is_anagram(candidate):
                result.append(candidate)

        return result

    def is_anagram(self, candidate):
        # Check if the sorted list of characters in both words is the same
        return sorted(candidate.lower()) == sorted(self.word.lower())
