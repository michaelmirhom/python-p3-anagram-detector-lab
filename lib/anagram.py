# your code goes here!
class Anagram:
    def __init__(self, word=None):
        self.word = word

    def match(self, word_list):
        # Initialize an empty list to store matching words
        matching_words = []

        # Iterate through each word in the word_list
        for word in word_list:
            # Check if the word is an anagram of the initialized word
            if self.is_anagram(self.word, word):
                # If it is an anagram, add it to the matching_words list
                matching_words.append(word)

        return matching_words

    def is_anagram(self, word1, word2):
        # Convert both words to lowercase for case-insensitive comparison
        word1 = word1.lower()
        word2 = word2.lower()

        # Check if the two words have the same characters when sorted
        return sorted(word1) == sorted(word2)

        

     



      
 
 
