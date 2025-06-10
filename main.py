import sys
from stats import word_count
from stats import num_of_chars

def get_book_text(file_path):

    with open(file_path) as f:

        file_contents = f.read()

    return file_contents


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:

        file_path = sys.argv[1]

        file_contents = get_book_text(file_path)

        word_num = word_count(file_contents)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_num} total words")
        print("----------- Character Count ----------")
        num_of_chars(file_contents)
        print("============= END ===============")

main()
