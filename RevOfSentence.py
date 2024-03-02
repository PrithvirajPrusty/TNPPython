def reverse_words(sentence):
    words = sentence.split()
    reverse = ' '.join(reversed(words))
    return reverse

# Example usage
S = "Just Tell Me A Simple Sentence"
res = reverse_words(S)
print(res)