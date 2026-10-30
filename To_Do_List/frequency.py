filename = "sample.txt"

with open(filename, "r") as f:

    text = f.read()


print(text[:200])

word_count = {}
words = text.split()

for word in words:
    if 