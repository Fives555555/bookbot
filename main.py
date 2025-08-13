

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
    """Print contents of text file to console

    Args:
        filepath (string): Path to text file to be read

    Returns:
        print(string): Prints contents of file as a string
    """
    return print(get_book_text(filepath))


main("books/frankenstein.txt")