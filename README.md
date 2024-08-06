
# Simplified `sed` Command in Python

This project implements a simplified version of the `sed` command, focusing on the substitution feature (`s/old/new/flags`). The script processes text by performing search-and-replace operations based on the provided patterns.

## Usage

```sh
python sed.py [-i] [-g] [-n] [-p] [-e] [-f scriptfile] 's/old/new/flags'... [file|string]
```

## Options

- `-i` : Edit files in place.
- `-g` : Global replacement (replace all occurrences).
- `-n` : Suppress automatic printing of the pattern space.
- `-p` : Print the result to stdout.
- `-e` : Allows for multiple substitution patterns.
- `-f` : Read patterns from a file.

## Arguments

- `patterns` : One or more substitution patterns in the format `'s/old/new/flags'`.
- `file|string` : The file or input string to apply the substitution.

## Functions

### `parse_arguments()`

Parses command-line arguments and extracts options, patterns, and input sources.

### `parse_pattern(pattern)`

Parses a substitution pattern in the format `'s/old/new/flags'`.

### `replace_text(old, new, text, flags)`

Replaces occurrences of a substring in a given text with a new substring, with optional case-insensitive and global replacement.

### `read_input(input_source)`

Reads input from a file or directly from a provided string.

### `write_output(file, content)`

Writes the given content to a file.

### `main()`

Main function to execute the sed-like utility:
1. Parses command-line arguments.
2. Reads the input text from the specified file or string.
3. Applies the text substitution patterns to the input text.
4. Writes the modified text to the original file if the `-i` option is provided and the input source is a file.
5. Prints the modified text to stdout if the `-p` option is provided, or if the `-i` option is not provided or the input source is not a file.

## Example

```sh
python sed.py -i 's/foo/bar/g' input.txt
```

This command will replace all occurrences of `foo` with `bar` in `input.txt` and save the changes in place.

## Author

[Itay Nachshon]
