"""
Word Occurrences
Estimate: 23 minutes
Actual:
"""

word_to_count = {}
text = "This is only an example text hello hi there hi there again this is still example text"
words = text.split()

for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

max_length = max(len(word) for word in words)

print(text)
for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")
