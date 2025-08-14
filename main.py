import sys
from stats import word_count, character_count, sort_dict

def get_book_text(filepath):
    """Return contents of text file as a string from the filepath

    Args:
        filepath (string): Path to text file to be read

    Returns:
        file_contents (string): Contents of file as a string
    """
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main(filepath):
    """Print report of word and alphabetical character count of text file to console

    Args:
        filepath (string): Path to text file to be read

    Returns:
        print(string): Prints report of word and alphabetical character count of text file
    """
    book_text = get_book_text(filepath)
    num_words = word_count(book_text)
    character_dict = character_count(book_text)
    sorted_list = sort_dict(character_dict)
    
    print(f"============ BOOKBOT ============ \nAnalyzing book found at {filepath}...")
    print(f"----------- Word Count ---------- \nFound {num_words} total words")
    print("--------- Character Count -------")
    
    for dict in sorted_list:
        if dict['char'].isalpha():
            print(f"{dict['char']}: {dict['num']}")
            
    print("============= END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])