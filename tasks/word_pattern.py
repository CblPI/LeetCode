# Link -> https://leetcode.com/problems/word-pattern
# Author: Ilya Shvarev

class Solution:
    @staticmethod
    def wordPattern(pattern: str, source: str) -> bool:
        words = source.split()
        if len(pattern) != len(words):
            return False

        char_set = {}
        word_set = {}

        for char, word in zip(pattern, words):
            if char in char_set:
                if char_set[char] != word:
                    return False
            else:
                char_set[char] = word

            if word in word_set:
                if word_set[word] != char:
                    return False
            else:
                word_set[word] = char

        return True