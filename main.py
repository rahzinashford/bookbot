from stats import word_count
from stats import num_of_chars

def get_book_text(file_path):

    with open(file_path) as f:

        file_contents = f.read()

    return file_contents


def main():

    file_contents = get_book_text("books/frankenstein.txt")

    word_num = word_count(file_contents)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_num} total words")
    print("----------- Character Count ----------")
    num_of_chars(file_contents)
    print("============= END ===============")

main()
