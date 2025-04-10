
# Problem Statement:
# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

def reverse_vowels(text):

  dtext = list(text)

  # O(1)
  vowels = set(list('aeiouAEIOU'))
  vowel_index = []

  for i, ch in enumerate(list(text)):
    if ch in vowels:
      vowel_index.append(i)

  j = len(vowel_index) - 1

  r = ''
  for i, ch in enumerate(dtext):
    if i in vowel_index:
      r += dtext[vowel_index[j]]
      j -= 1
    else:
      r += ch

  return r

text = 'DesignGUrus'
print(reverse_vowels(text))

text = 'hello'
print(reverse_vowels(text))

text = 'AEIOU'
print(reverse_vowels(text))


