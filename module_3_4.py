def single_root_words(root_word, *other_words):
    same_words = []
    root_word_new = root_word.lower()
    for i in other_words:
        i_new = i.lower()
        if root_word_new in i_new or i_new in root_word_new:
            same_words.append(i)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
