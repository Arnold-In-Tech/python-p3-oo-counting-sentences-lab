#!/usr/bin/env python3
import re

class MyString:

  def __init__(self, value=''):
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if (type(value) == str):
      self._value = value
    else:
      print("The value must be a string.")
  
  def is_sentence(self):
    if (self.value[-1] == "."):
      return True
    else:
      return False
    
  def is_question(self):
    if self.value.endswith("?"):
      return True
    else:
      return False

  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    else:
      return False


  # print(re.escape(".!?"))   # print escape pattern to be used with split  
  def count_sentences(self):
    sentences_list = re.split("\. |! |\?", self.value)     # Regex pattern splits on substrings ". " , "! "and "! "
    sentences_count = len(list(filter(None, sentences_list)))     # remove empty sentences and count
    return sentences_count


# test code
string = MyString()
string.value = "This, well, is a sentence. This is too!! And so is this, I think? Woo..."
string.count_sentences()

