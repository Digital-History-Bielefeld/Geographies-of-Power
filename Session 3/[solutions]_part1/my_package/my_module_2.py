def remove_vowels(text):
  vowels = ['a', 'e', 'i', 'o', 'u']
  for vowel in vowels:
    text = text.replace(vowel, "")

  return text 
