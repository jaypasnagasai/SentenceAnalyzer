# Sentence Word Statistics Analyzer

This Python script analyzes a given sentence and provides various statistics about the words in the sentence. It calculates the total number of words, the number of unique words, the average word length, and the frequency of each word. Additionally, it identifies the longest and shortest words in the sentence.

## Usage

1. Make sure you have Python installed on your system.
2. Clone or download this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/sentence-word-stats.git
   ```

1. Navigate to the project directory:
   
   ```
   cd sentence-word-stats
   ```

2. Run the script:
   
   ```
   python sentence_stats.py
   ```
3. Enter a sentence when prompted. The script will then process the input and display the word statistics.

## Features

Calculates the total number of words in the sentence.
Determines the number of unique words in the sentence.
Computes the average word length in the sentence.
Generates a frequency count of each word using the `Counter` class.
Identifies the longest and shortest words in the sentence.

## Example

Let's say you run the script and enter the sentence: "The quick brown fox jumps over the lazy dog."

The script will output:
```
Enter a sentence: The quick brown fox jumps over the lazy dog.
Number of all words in the sentence: 9
Number of unique words in the sentence: 8
Average word length: 4.444444444444445
Longest word: jumps
Shortest word: The
Word Frequency: Counter({'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1})
```

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or a pull request in this repository.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
