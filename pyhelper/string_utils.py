
def reverse_text(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text[::-1]


def is_palindrome(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def count_words(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return len(text.split())


def count_vowels(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    return sum(1 for char in text.lower() if char in "aeiou")


def capitalize_words(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.title()


def remove_whitespace(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return "".join(text.split())
