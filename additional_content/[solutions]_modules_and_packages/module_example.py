# import my_module
from my_module import lowercase_and_without_whitespaces
from my_package.my_module_2 import remove_vowels

text = "   HELLO   !   "
text2 = "I want to remove all vowels from this text!"

# new_text = my_module.lowercase_and_without_whitespaces(text)
lowercase_text_without_whitespaces = lowercase_and_without_whitespaces(text)
print(lowercase_text_without_whitespaces)  # hello!

text_without_vowels = remove_vowels(text2)
print(text_without_vowels)  # wnt t rmv ll vwls frm ths txt!



