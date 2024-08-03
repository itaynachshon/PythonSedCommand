
# Simplified `sed` Utility

## Description

This project implements a simplified version of the `sed` utility in Python. It allows for basic text substitution operations similar to those provided by the Unix `sed` command.

## Features

- **In-place editing**: Modify files directly.
- **Global replacement**: Replace all occurrences of a pattern.
- **Suppress automatic printing**: Control the output of the pattern space.
- **Print result**: Output the result to standard output.
- **Multiple substitution patterns**: Apply multiple substitution patterns in a single command.

## Usage

The script can be run using the following command:

\`\`\`bash
python sed.py [-i] [-g] [-n] [-p] [-e 's/old/new/flags']... [file|string]
\`\`\`

### Options:

- \`-i\`: Edit files in place.
- \`-g\`: Global replacement (replace all occurrences).
- \`-n\`: Suppress automatic printing of pattern space.
- \`-p\`: Print the result to stdout.
- \`-e\`: Allows for multiple substitution patterns.

### Example:

\`\`\`bash
python sed.py -i -e 's/old/new/g' -e 's/foo/bar/i' input.txt
\`\`\`

## Installation

1. Clone the repository:

\`\`\`bash
git clone <repository-url>
cd <repository-directory>
\`\`\`

2. Ensure you have Python installed (Python 3.x is recommended).

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the directory where \`sed.py\` is located.
3. Execute the script with the desired options and arguments as shown in the usage section.

## Functions

- \`parse_arguments()\`: Parses command-line arguments.
- \`parse_pattern(pattern)\`: Parses the substitution pattern.
- \`replace_text(old, new, text, flags)\`: Replaces occurrences of a substring in a given text with a new substring.
- \`read_input(input_source)\`: Reads input from a file or directly from a provided string.
- \`write_output(file, content)\`: Writes the given content to a file.
- \`main()\`: Main function to execute the sed-like utility.

## Left to be Implemented:

- Read string (after echo and pipe or using EOF or simply entering text).
- Implement \`-n\` and \`-p\` options.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository.
2. Create a new branch (\`git checkout -b feature-branch\`).
3. Commit your changes (\`git commit -am 'Add new feature'\`).
4. Push to the branch (\`git push origin feature-branch\`).
5. Create a new Pull Request.

## Contact

For any questions or suggestions, please open an issue in the repository.

---

This README provides an overview of the project, its usage, and how to contribute. For more detailed information, refer to the function docstrings in the \`sed.py\` file.
