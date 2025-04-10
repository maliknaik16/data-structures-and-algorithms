
# Problem Statement:
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
# non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.

def validPalindrome(text):
  dtext = list(text)

  cleaned_text = ''

  for ch in dtext:
    ch = ch.lower()

    if ch.isalpha():
      cleaned_text += ch

  if cleaned_text == cleaned_text[::-1]:
    return True

  return False

sentence = "A man, a plan, a canal, Panama!"
print(validPalindrome(sentence))

sentence = "Was it a car or a cat I saw?x?"
print(validPalindrome(sentence))
