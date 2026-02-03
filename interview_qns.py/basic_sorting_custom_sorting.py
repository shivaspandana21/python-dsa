#Basic & Custom Sorting
def sort_alpha(words):
    return sorted(words)

def sort_by_length(words):
    return sorted(words, key=len)