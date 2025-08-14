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

def sort_on(items):
    """Function to take a dictionary and return the value of the "num" key. This is for the .sort() method to use to sort a list of dictionaries

    Args:
        items (dict): A dictionary with a "num" key

    Returns:
        int: value of "num" key 
    """
    return items["num"]

def sort_dict(dict):
    """Take a dictionary of characters and their counts and return a sorted list of dictionaries from greatest number of characters to least

    Args:
        dict (dict): Dictionary of characters and their counts

    Returns:
        list: List of dictionaries sorted from greatest to least by count
    """
    dict_list = []
    for item in dict:
        temp_dict = {"char": item, "num": dict[item]}
        dict_list.append(temp_dict)
        
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list