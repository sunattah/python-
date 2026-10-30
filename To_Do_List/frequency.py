filename = "sample.txt"

with open(filename, "r") as f:

    text = f.read()


print(text[:200])

word_count = {}
words = text.split()

for word in words:
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