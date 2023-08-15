# Import necessary libraries
import re
from collections import Counter

# Get input from the user (sentence)
sentence = input("Enter a sentence: ")

# Check if the input sentence is not empty
if not sentence:
    print("Please enter a sentence.")
else:
    # Convert the sentence to lowercase
    sentence_lower = sentence.lower()

    # Use regular expressions to find all words in the sentence
    words = re.findall(r'\w+', sentence_lower)

    # Calculate word statistics
    all_word_count = len(words)  # Total number of words in the sentence
    unique_word_count = len(set(words))  # Number of unique words in the sentence
    avg_word_length = sum(len(word) for word in words) / all_word_count  # Average word length

    # Calculate word frequency using Counter
    word_frequency = Counter(words)  # A dictionary-like object containing word frequencies

    # Identify longest and shortest words
    longest_word = max(words, key=len)  # The word with the maximum length
    shortest_word = min(words, key=len)  # The word with the minimum length

    # Print the results
    print("Number of all words in the sentence:", all_word_count)
    print("Number of unique words in the sentence:", unique_word_count)
    print("Average word length:", avg_word_length)
    print("Longest word:", longest_word)
    print("Shortest word:", shortest_word)
    print("Word Frequency:", word_frequency)
