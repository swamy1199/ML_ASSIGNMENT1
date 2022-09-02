string = "I am a teacher and I love to inspire and teach people"
# Splitting the given string
words_string = string.split(" ")
counts = dict()
unique_words = []
# using for loop checking each element in list is unique or any duplicates are present in list
for word in words_string:
    if word in unique_words:
        counts[word] += 1
    else:
        # Assiging 1 to each unique word and finding length from i
        counts[word] = 1
print(len(counts))