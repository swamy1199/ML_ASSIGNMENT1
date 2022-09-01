string = "I am a teacher and I love to inspire and teach people"
words_string = string.split(" ")
counts = dict()
unique_words = []
for word in words_string:
    if word in unique_words:
        counts[word] += 1
    else:
        counts[word] = 1
print(len(counts))