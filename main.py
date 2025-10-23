import sys
from stats import count_words
from stats import count_chars
from stats import report

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()

    char_dict = count_chars(file_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(file_contents)} total words")
    print("--------- Character Count -------")
    book_stats = report(char_dict)
    for item in book_stats:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
        else:
            continue
    print("============= END ===============")
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    get_book_text(sys.argv[1])
    

main()