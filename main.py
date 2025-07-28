from stats import count_words, count_chars, print_report

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    

def main():
    words = get_book_text("books/frankenstein.txt")
    total_words = count_words(words)
    char_dict = count_chars(words.lower())
    print_report(total_words, char_dict)

main()

