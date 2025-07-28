from collections import Counter

def count_words(words):
    word_count = 0
    each_words = words.split()
    for x in each_words:
        word_count +=1
    return word_count

def count_chars(words):
    char_count = Counter(words)

    return(dict(char_count))

def print_report(word_count, char_count):
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for x in char_count:
        print(x.values)
        #print(sorted(char_count.items()))



