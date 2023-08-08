def capital_letter(s):
    words = s.split()
    if len(words) > 0:
        words[0] = words[0][0].upper() + words[0][1:]
    for i in range(1, len(words)):
        if words[i - 1][1] in ".!?":
            words[i] = words[i][0].upper() + words[i][1:]
    return "".join(words)


def upper_first_letter(s):
    """The function for capitalizes the first letters of each word in a string. """
    words = s.split()
    return words[0].upper()
