
s = input("Enter a sentence: ")
words = s.lower().split()

for word in words:
    if words.count(word) > 1:
        print(word, "is repeated")
        words = [w for w in words if w != word]
