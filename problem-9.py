# Problem-7 Write a python function that accepts a string as input and returns the word with most occurence.

# Input:
# hello how are you i am fine thank you

# Output
# you -> 2


def word_count(text):
    words = text.split()
    counts = dict()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    max_word = ''
    max_count = 0

    for word, count in counts.items():
        if count > max_count:
            max_count = count
            max_word = word
    return max_word, max_count, counts

print(word_count('hello how are you i am fine thank you'))