def word_count(filecontents):
    """Count the number of words in a string

    Args:
        filecontents (string): Contents of a file as a string

    Returns:
        int: Number of words in the input string
    """
    return len(filecontents.split())

def character_count(filecontents):
    """Count the number of characters in a file

    Args:
        filecontents (string): File contents as a string

    Returns:
        dict: Dictionary containing keys for each character and the value being the count for each character
    """
    character_dict = {}
    for character in filecontents.lower():
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1

    return character_dict