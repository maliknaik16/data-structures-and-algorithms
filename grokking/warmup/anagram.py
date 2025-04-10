
# Problem Statement:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
# the original letters exactly once.

def validAnagram(s: str, t: str):

  if len(s) != len(t):
    return False

  char_map = {}

  for ch in s:
    if ch not in char_map:
      char_map[ch] = 0

    char_map[ch] += 1

  for ch in t:
    if ch not in char_map:
      return False

    char_map[ch] -= 1

    if char_map[ch] == 0:
      del char_map[ch]

  if len(char_map) == 0:
    return True

  return False

s = 'listen'
t = 'silent'
print(validAnagram(s, t))

s = "rat"
t = "car"
print(validAnagram(s, t))

s = "hello"
t = "world"
print(validAnagram(s, t))

