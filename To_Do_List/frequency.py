filename = "sample.txt"

with open(filename, "r") as f:

    text = f.read()


print(text[:200])

word_count = {}
words = text.split()

for word in words:
    if len(word) == 0:
        continue
    if word in word_count:
        word_count[word] + 1
    else:
        word_count[word] = 1
        print(word_count)
    text = text.lower()

    text = text.replace(".", "")    
    text = text.replace(",", "")    
    text = text.replace("!", "")    
    text = text.replace("?", "")
    text = text.replace(";", "")
    text = text.replace(":", "")
    text = text.replace('"', "")
    text = text.replace("(", "")
    text = text.replace(")", "")
    text = text.replace("_", "")
    text = text.replace("-", "")
word_list = list(word_count.items())

sorted_words = sorted(word_list, key=len, reverse=True)
top_10 = sorted_words[:10]
print("Top 10 words")

for rank, (word, count) in enumerate(top_10, start=1):
    print(f"{rank}. {word} - {count}")

    letter_count = {}

    for char in text:
        if char.isalpha():
            char = char.lower()
        else:
            continue
        if char in letter_count:
            letter_count[char] + 1
        else:
            letter_count[char] = 1
            print(letter_count)
            