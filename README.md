# Explanation
 I have used Tries Insert and Search for this question because the search complexities can be brought to optimal limit generally use trie's to store strings.

Each node of a trie consists of two things:

A character

A boolean value is used to implement whether this character represents the end of the word.

Each character can have 26 references.Nodes in a trie do not store entire keys, instead, they store a character of the string. When we traverse down from the root node to the leaf node, we can build the key from these small parts of the key.

