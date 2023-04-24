class StringUtility:

    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def upper(self):
        return self.string.upper()

    def lower(self):
        return self.string.lower()

    def capitalize(self):
        return self.string.capitalize()

    def title(self):
        return self.string.title()

    def strip(self):
        return self.string.strip()

    def lstrip(self):
        return self.string.lstrip()

    def rstrip(self):
        return self.string.rstrip()

    def replace(self, old, new):
        return self.string.replace(old, new)

    def split(self, sep):
        return self.string.split(sep)

    def join(self, iterable):
        return self.string.join(iterable)

    def find(self, sub):
        return self.string.find(sub)

    def index(self, sub):
        return self.string.index(sub)

    def count(self, sub):
        return self.string.count(sub)

    def len(self):
        return len(self.string)

    def format(self, *args, **kwargs):
        return self.string.format(*args, **kwargs)

    def vowels(self):
        count = 0
        for char in self.string:
            if char in "aeiouAEIOU":
                count += 1
        if count < 5:
            return str(count)
        else:
            return "many"

    def bothEnds(self):
        if len(self.string) <= 2:
            return ""
        else:
            return self.string[0:2] + self.string[-2:]

    def fixStart(self):
        if not self.string:
            return ""

        first_char = self.string[0]
        new_string = first_char
        for char in self.string[1:]:
            if char == first_char:
                new_string += "*"
            else:
                new_string += char
        return new_string


    def asciiSum(self):
        total = 0
        for char in self.string:
            total += ord(char)
        return total

    def cipher(self):
        encoded = ""
        length = len(self.string)
        for letter in self.string:
            if letter.isalpha():
                ascii_value = ord(letter)
                offset = length % 26
                if letter.isupper():
                    ascii_value = (ascii_value - ord('A') + offset) % 26 + ord('A')
                else:
                    ascii_value = (ascii_value - ord('a') + offset) % 26 + ord('a')
                encoded += chr(ascii_value)
            else:
                encoded += letter
        return encoded

