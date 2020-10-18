n = int(input())

synonyms = {}

for _ in range(n):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for word, synonym in synonyms.items():
    print(f"{word} - {', '.join(synonym)}")

