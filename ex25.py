def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts words"""
    return sorted(words)

def print_first_word(words):
    return words.pop(0)

def print_last_word(words):
    return words.pop(-1)

def sort_sentence(sentence):
    words = break_words(sentence)
    return sort_words
