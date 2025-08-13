def word_count(filecontents):
    """Count the number of words in a string

    Args:
        filecontents (string): Contents of a file as a string

    Returns:
        int: Number of words in the input string
    """
    return len(filecontents.split())
