def all_variants(text):
    length = len(text)
    for start in range(1, length + 1):
        for end in range(length - start + 1):
            yield text[end: end + start]

a = all_variants('abc')
for i in a:
    print(i)
