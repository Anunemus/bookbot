def count_words(words):
    word_count = 0
    each_words = words.split()
    for x in each_words:
        word_count +=1
    print(f"{word_count} words found in the document")

