# # Left to be implemented:
# #     - read string (after echo and pipe or using EOF or simply entering text)
# #     - -n \p option.
import os
import re
import sys

def parse_arguments():
    """
    Parses command-line arguments for a simplified sed utility.

    This function reads the command-line arguments provided to the script and
    extracts the options, substitution patterns, file name, or input string. It ensures that
    the required arguments are present and in the correct format, otherwise it
    exits the program with an error message.

    The expected usage is:
    python sed.py [-i] [-g] [-n] [-p] [-e] ['s/old/new/flags']... [file|string]

    Options:
    -i : Edit files in place.
    -g : Global replacement (replace all occurrences).
    -n : Suppress automatic printing of pattern space.
    -p : Print the result to stdout.
    -e : Allows for multiple substitution patterns.

    Returns:
        tuple: A tuple containing:
            patterns (list): A list of substitution patterns in the format 's/old/new/flags'.
            input_source (str): The name of the file or the input string to apply the substitution.
            options (list): A list of options (e.g., ['-i', '-g']).

    Exits:
        If the number of arguments is less than 3 or if the pattern or input source
        is not provided, it prints the usage message and exits the program.
    """
    if len(sys.argv) < 3:
        print("Usage: python (or python3) sed.py [-i] [-g] [-n] [-p] [-e] 's/old/new/flags']... [file|string]")
        sys.exit(1)
    
    options = []
    patterns = []
    input_source = None

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg.startswith('-'):
            if arg == '-e': # parsing the following pattern after -e
                i += 1
                if i < len(sys.argv):
                    patterns.append(sys.argv[i])
                else:
                    print("Usage: python (or python3) sed.py [-i] [-g] [-n] [-p] [-e] 's/old/new/flags']... [file|string]")
                    sys.exit(1)
            else:
                options.append(arg)
        elif arg.startswith('s/') and '/' in arg[2:]: # gets the pattern
            patterns.append(arg)
        elif input_source is None: # if didn't catch input_source yet and doesn't follow the other conditions- its an input_source
            input_source = arg
        else:
            print("Usage: python (or python3) sed.py [-i] [-g] [-n] [-p] [-e] 's/old/new/flags']... [file|string]")
            sys.exit(1)
        i += 1

    if not patterns or not input_source:
        print("Usage: python (or python3) sed.py [-i] [-g] [-n] [-p] [-e] 's/old/new/flags']... [file|string]")
        sys.exit(1)

    return patterns, input_source, options

def parse_pattern(pattern):
    """
    Parses the substitution pattern.

    This function parses the substitution pattern provided to the script.
    The expected pattern format is 's/old/new/flags'.

    Args:
        pattern (str): The substitution pattern in the format 's/old/new/flags'.

    Raises:
        ValueError: If the given input doesn't match the expected pattern format.

    Returns:
        tuple: A tuple containing the old text, the new text (that will replace the old one), 
               and the flags.
    """
    match = re.match(r's/(.*?)/(.*?)/([gip]*)/?$', pattern)
    if not match:
        # Split to 2 different errors in case of no matches:
        if pattern.endswith('/'):
            raise ValueError(f"python sed: 1: \"{pattern}\": bad flag in substitute command: '/'")
        else:
            raise ValueError(f"python sed: 1: \"{pattern}\": unterminated substitute in regular expression")
    old, new, flags = match.groups()
    # Verify the syntax of the regex (whether there is a '/' in the end of flags or the 'new' variable).
    if flags and pattern[-1] == '/':
        raise ValueError(f"python sed: 1: \"{pattern}\": bad flag in substitute command: '/'")
    if not flags and pattern[-1] != '/':
        raise ValueError(f"python sed: 1: \"{pattern}\": unterminated substitute in regular expression")
    return old, new, flags

def replace_text(old, new, text, flags):
    """
    Replaces occurrences of a substring in a given text with a new substring,
    with optional case-insensitive and global replacement.

    Args:
        old (str): The substring to be replaced.
        new (str): The substring to replace with.
        text (str): The text in which to perform the replacement.
        flags (str): A string containing optional flags:
            - 'i' for case-insensitive replacement.
            - 'g' for global replacement (replace all occurrences).

    Returns:
        str: The text with the specified replacements made.
    """
    re_flags = 0
    if 'i' in flags:
        re_flags |= re.IGNORECASE # Using bitwise OR operation. Could also used re_flags = re.IGNORECASE but bitwiseOR is more scalable.
    if 'g' in flags:
        return re.sub(old, new, text, flags=re_flags)
    else:
        return re.sub(old, new, text, count=1, flags=re_flags)

def read_input(input_source):
    """
    Reads input from a file or directly from a provided string.

    This function reads the contents from a specified file or from a provided input string.

    Args:
        input_source (str): The path to the file to be read or the input string.

    Returns:
        str: The content of the file or the input string.
    """
    if input_source == '-':
        return sys.stdin.read()
    elif os.path.isfile(input_source):
        with open(input_source, 'r') as f:
            return f.read()
    else:
        return input_source

def write_output(file, content):
    """
    Writes the given content to a file.

    Args:
        file (str): The path to the file to be written.
        content (str): The content to write to the file.
    """
    with open(file, 'w') as f:
        f.write(content)

def main():
    """
    Main function to execute the sed-like utility.

    This function parses command-line arguments, reads the input file or string,
    performs the text substitution, and either writes the result to the file or
    prints it to stdout based on the provided options.

    Steps:
    1. Parse command-line arguments to extract patterns, input source, and options.
    2. Read the input text from the specified file or string.
    3. Apply the text substitution patterns to the input text.
    4. Write the modified text to the original file if the '-i' option is provided and the input source is a file.
    5. Print the modified text to stdout if the '-p' option is provided, or if the '-i' option is not provided or the input source is not a file.
    """
    patterns, input_source, options = parse_arguments()
    input_text = read_input(input_source)

    for pattern in patterns:
        try:
            old, new, flags = parse_pattern(pattern)
            input_text = replace_text(old, new, input_text, flags)
        except ValueError as e:
            sys.stderr.write(str(e) + '\n')
            sys.exit(1)
    
    is_file = os.path.isfile(input_source)
    if '-i' in options and is_file:
        write_output(input_source, input_text)

    if '-p' in options or '-i' not in options or not is_file:
        sys.stdout.write(input_text)

if __name__ == '__main__':
    main()
