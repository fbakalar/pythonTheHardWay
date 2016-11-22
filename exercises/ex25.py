##################################################
#
#   Exerciae 25
#
#    Even MORE practice
#
#     functions and variables
#
##################################################

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

print break_words('something or something else') #example of break_words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

print sort_words("just a random list of words")

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    return word
 #   print word

def print_second_word(words2):
    """Prints the first word after popping it off."""
    word = words2.pop(0)
    return word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    return word

sentance = break_words('something or anything else')
print sentance
print print_last_word(sentance)
print sentance
print print_first_word(sentance)
print sentance
print print_second_word(sentance)
print sentance