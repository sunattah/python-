
filename = "sample.txt"

with open(filename, "r", encoding="utf-8") as f:
    text = f.read()

print("First 200 characters:")
print(text[:200])
print("-" * 40)

text = text.lower()

for char in '.,!?;:"()_-–—\'':
    text = text.replace(char, "")

word_count = {}
words = text.split()

for word in words:
    if word:  # skip empty strings
        word_count[word] = word_count.get(word, 0) + 1

sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
top_10 = sorted_words[:10]

print("\nTop 10 most frequent words:")
for rank, (word, count) in enumerate(top_10, start=1):
    print(f"{rank:2}. {word} - {count}")

letter_count = {}

for char in text:
    if char.isalpha():
        letter_count[char] = letter_count.get(char, 0) + 1

sorted_letters = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)

print("\nLetter frequencies (highest first):")
for rank, (letter, count) in enumerate(sorted_letters, start=1):
    print(f"{rank:2}. {letter} → {count}")