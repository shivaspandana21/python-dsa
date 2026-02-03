#13. Word Ordered Problem
#Q1: Alphabetical order
def sort_words_alpha(sentence):
    return " ".join(sorted(sentence.split()))

#Q2: Sort by length
def sort_words_length(sentence):
    return " ".join(sorted(sentence.split(), key=len))