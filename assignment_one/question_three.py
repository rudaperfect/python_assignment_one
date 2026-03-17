def lookup(dictionary, search_term):
    matches = []

    # Convert search term to lowercase
    search_term = search_term.lower()

    # Check each key in the dictionary
    for key in dictionary:
        if search_term in key.lower():
            matches.append(key)

    # No matches found
    if len(matches) == 0:
        raise KeyError("search term not found")

    # Multiple matches found
    if len(matches) > 1:
        raise KeyError("multiple keys found")

    # Exactly one match
    key = matches[0]
    return key, dictionary[key]


# Example
fruit = {"apple": 1, "banana": 2}

print(lookup(fruit, "NANA"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
