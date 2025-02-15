def main():
    path_to_file = "books/frankenstein.txt"
    
    with open(path_to_file, "r") as f:  # Open the file in read mode
        file_contents = f.read()  # Read the entire contents into a string

    word_count = count_words(file_contents)  # Count words in the text
    char_counts = count_characters(file_contents)  # Count character occurrences

    print_report(path_to_file, word_count, char_counts)  # Print the report


def count_words(text):
    """Takes a string and returns the number of words."""
    words = text.split()  # Split the text into words
    return len(words)  # Return the number of words


def count_characters(text):
    """Takes a string and returns a dictionary of character frequencies (case-insensitive)."""
    text = text.lower()  # Convert text to lowercase
    char_counts = {}  # Initialize dictionary
    
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts  # Return the dictionary of character counts


def print_report(file_path, word_count, char_counts):
    """Prints a formatted report of word and character frequency."""
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")

    # Convert dictionary to list of tuples and sort by frequency (descending)
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)

    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


if __name__ == "__main__":
    main()
