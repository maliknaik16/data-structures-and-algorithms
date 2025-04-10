
# Problem Statement:
# A pangram is a sentence where every letter of the English alphabet appears at least once.
#
# Given a string sentence containing English letters (lower or upper-case), return true if sentence is a pangram, or
# false otherwise.
#
# Note: The given sentence might contain other characters like digits or spaces, your solution should handle these too.

def isPangram(sentence):
  """
  Time Complexity: O(n)
  Space Complexity: O(1)
  """
  english_alphabets = set(list('abcdefghijklmnopqrstuvwxyz'))

  for ch in list(sentence):
    ch = ch.lower()

    if ch in english_alphabets:
      english_alphabets.remove(ch)

  return len(english_alphabets) == 0

sentence = "TheQuickBrownFoxJumpsOverTheLazyDog"
print(sentence)
print(isPangram(sentence))

sentence = "This is not a pangram"
print(sentence)
print(isPangram(sentence))
