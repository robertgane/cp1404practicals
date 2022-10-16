"""
CP1404 Practical 5
Word Occurrences
Estimate: 10 minutes
Actual: 7 minutes
"""

word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
max_length = max(len(word) for word in word_to_count)
for word, count in sorted(word_to_count.items()):
    print(f"{word:{max_length}} : {count}")
