
# Problem:
# Given an array of strings words and two different strings that already exist in the array word1 and word2,
# return the shortest distance between these two words in the list.

def shortest_word_distance(words, a, b):
  i = -1
  j = -1

  dist = float('inf')

  for k, word in enumerate(words):
    if word == a:
      i = k

    if word == b:
      j = k

    if i != -1 and j != -1:
      dist = min(dist, abs(j - i))

  return dist




words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
word1 = "fox"
word2 = "dog"

print(shortest_word_distance(words, word1, word2))

words = ["a", "b", "c", "d", "e"]
word1 = "a"
word2 = "e"

print(shortest_word_distance(words, word1, word2))

words = ["a", "c", "d", "b", "a"]
word1 = "a"
word2 = "b"

print(shortest_word_distance(words, word1, word2))

words = ["repeated", "words", "in", "the", "array", "words"]
word1 = "repeated"
word2 = "words"

print(shortest_word_distance(words, word1, word2))

