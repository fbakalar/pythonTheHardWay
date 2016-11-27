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
    return sorted(words)   #can <words> be a string?

print sort_words("just a random list of words")

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
 #   return word
    print word

def print_second_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    return word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
 #   return word
    print word

sentence = break_words('something or anything else')
print sentence
print print_last_word(sentence)
print sentence
print print_first_word(sentence)
print sentence
print print_second_word(sentence)
print sentence

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

print "sort_sentence"
print sort_sentence(' this is the sentence to use')

def print_first_and_last(sentence):  
# notice there is no <return> statement needed here
    """Prints the first and last words of the sentence."""
    words2 = break_words(sentence)
    print_first_word(words2)
    print_last_word(words2)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)









