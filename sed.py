import re
import sys

def parse_arguments():
    if len(sys.argv) < 3:
        print("Usage: python script.py [-i] [-g] [-n] [-p] 's/old/new/flags' file")
        sys.exit(1)
    options = []
    pattern = None
    file = None

    for arg in sys.argv[1:]:
        if arg.startswith('-'):
            options.append(arg)
        elif pattern is None:
            pattern = arg
        else:
            file = arg

    if not pattern or not file:
        print("Usage: python script.py [-i] [-g] [-n] [-p] 's/old/new/flags' file")
        sys.exit(1)

    return pattern, file, options

def parse_pattern(pattern):
    match = re.match(r's/(.*)/(.*)/([gip]*)', pattern)
    if not match:
        raise ValueError("Invalid pattern format. Expected 's/old/new/flags'.")
    old, new, flags = match.groups()
    return old, new, flags

def replace_text(old, new, text, flags):
    re_flags = 0
    if 'i' in flags:
        re_flags |= re.IGNORECASE
    if 'g' in flags:
        return re.sub(old, new, text, flags=re_flags)
    else:
        return re.sub(old, new, text, count=1, flags=re_flags)

def read_input(file):
    if file == '-':
        return sys.stdin.read()
    else:
        with open(file, 'r') as f:
            return f.read()

def write_output(file, content):
    with open(file, 'w') as f:
        f.write(content)

def main():
    pattern, file, options = parse_arguments()
    old, new, flags = parse_pattern(pattern)
    input_text = read_input(file)
    result = replace_text(old, new, input_text, flags)
    
    if '-i' in options:
        write_output(file, result)

    if '-p' in options or '-i' not in options:
        sys.stdout.write(result)

if __name__ == '__main__':
    main()
