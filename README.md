# Explanation
I have imported os for handling the files and I also have impoted sys to fetch the data from both the inputs i.e (input_01.txt and input_02.txt).

I have used Tries Insert and Search for this question because the search complexities can be brought to optimal limit generally use trie's to store strings.
Each node of a trie consists of two things:

A character

A boolean value is used to implement whether this character represents the end of the word.

Each character can have 26 references.Nodes in a trie do not store entire keys, instead, they store a character of the string. When we traverse down from the root node to the leaf node, we can build the key from these small parts of the key.

#Output from both the test cases :

![image](https://user-images.githubusercontent.com/85862040/155889429-0fea807f-7bd2-41b3-84a3-5a4f30031039.png)
![image](https://user-images.githubusercontent.com/85862040/155889433-69e7d729-1bf5-4a57-a619-7aede035450f.png)
