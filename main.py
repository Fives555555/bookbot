from stats import word_count

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
    """Print word count of text file to console

    Args:
        filepath (string): Path to text file to be read

    Returns:
        print(string): Prints word count of file
    """
    num_words = word_count(get_book_text(filepath))
    return print(f"{num_words} words found in the document")


main("books/frankenstein.txt")