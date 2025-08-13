from stats import word_count, character_count

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
    """Print word and character count of text file to console

    Args:
        filepath (string): Path to text file to be read

    Returns:
        print(string): Prints word and character count of file
    """
    num_words = word_count(get_book_text(filepath))
    character_dict = character_count(get_book_text(filepath))
    
    print(f"{num_words} words found in the document")
    print(f"Character count: \n {character_dict}")

main("books/frankenstein.txt")