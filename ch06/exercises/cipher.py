def cipher(text):

    # Create a table of 26 characters, each with a unique substitution.
    substitutions = {
       'a': 'b',
        'b': 'c',
        'c': 'd',
        'd': 'e',
        'e': 'f',
        'f': 'g',
        'g': 'h',
        'h': 'i',
        'i': 'j',
        'j': 'k',
        'k': 'l',
        'l': 'm',
        'm': 'n',
        'n': 'o',
        'o': 'p',
        'p': 'q',
        'q': 'r',
        'r': 's',
        's': 't',
        't': 'u',
        'u': 'v',
        'v': 'w',
        'w': 'x',
        'x': 'y',
        'y': 'z',
        'z': 'a',
        ' ': 'W',
        'T': '1'
    }

   
    result = ''
    for char in text:
        result += substitutions[char]

    return result


def main():

    encrypted = cipher('The quick brown fox jumps over the lazy dog')

    with open(r'C:\Users\trost\github-classroom\bucs110SPRING23\portfolio-David-Trost\ch06\exercises\encrypted.txt', 'w') as f:
        f.write(encrypted)


if __name__ == '__main__':
    main()