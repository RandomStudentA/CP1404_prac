
counts = dict()

text = input("Text: ");
text = text.split()
for word in text:
    counts[word] = counts.get(word, 0) + 1


for word in sorted(counts):
    print("{:{}} : {}".format(word, 10, counts[word]))

