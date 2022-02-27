import os
import sys


class Node:
    def __init__(self, letter=None, isTerminal=False):
        self.letter = letter
        self.isTerminal = isTerminal
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()
        self.counts = {}

    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node(letter)
            current = current.children[letter]
        current.isTerminal = True

    def __contains__(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.isTerminal

    # Returns how many sub-words can make up the word, as well as the sub-words that make up the big word
    def decompose(self, word):
        # Do not accept the empty string ''
        if not word:
            return 0, []
        # Check if we've seen this word before
        if word in self.counts:
            return self.counts[word]
        # If not then we need to start traversing the trie
        current = self.root
        for index, letter in enumerate(word):
            if letter not in current.children:
                return 0, []
            current = current.children[letter]
            if current.isTerminal:
                suffix = word[index + 1:]  # Get the suffix
                suffix_count, suffix_list = self.decompose(suffix)  # decompose the suffix
                self.counts[suffix] = suffix_count, suffix_list  # store count for memoization
                if suffix_count:  # if suffix is decomposable
                    # add prefix to suffix list, add 1 to suffix count and return
                    return 1 + suffix_count, [word[:index + 1]] + suffix_list
        return current.isTerminal, [word]

    # Returns (isCompound, # small words, list of small words)
    def getCompound(self, word):
        decompose_num, decompose_list = self.decompose(word)
        return decompose_num > 1, decompose_num, decompose_list


def load(filename):
    words = []
    trie = Trie()
    with open(filename, 'r') as f:
        for line in f:
            word = line.strip()
            trie.insert(word)
            words.append(word)
    return trie, words


def processList(compoundList):
    compoundList.sort(key=lambda tup: len(tup[0]), reverse=True)
    return compoundList


def getCompoundList(trie, words):
    compound = []
    for word in words:
        isValid, num, dlist = trie.getCompound(word)
        if isValid:
            compound.append((word, num, dlist))
    return compound


def example(filename='words.txt'):
    trie, words = load(filename)
    compoundList = processList(getCompoundList(trie, words))

    # returns prints longest compound word if it exists
    longestWord = compoundList[0][0]
    secondLongestWord = compoundList[1][0]

    if len(longestWord):
        print("Longest compound word found is: \t\"" + longestWord + "\"")
        
    else:
        print("No largest compound words exist in this list.")
    if len(secondLongestWord):
        print("Second Longest compound word found is: \t\"" + secondLongestWord + "\"")
        
    else:
        print("No second largest compound words exist in this list.")


    return trie, words, compoundList


def main(argv):
    a = int(input())
    if a == 1:
        filename = "input_01.txt"
    elif a == 2:
        filename = "input_02.txt"
    example(filename)


if __name__ == "__main__":
    main(sys.argv)