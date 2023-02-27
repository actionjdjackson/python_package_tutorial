import re

class Phrase:
    """A class to represent phrases"""

    def __init__(self, content):
        self.content = str(content)

    def ispalindrome(self):
        """Return True for a palindrome, False otherwise"""
        if self._processed_content() == "":
            return False
        else:
            return self._processed_content() == reverse(self._processed_content())

    def _processed_content(self):
        """Process content for plaindrome testing"""
        return self.letters_and_digits().lower()

    def louder(self):
        """Change phrase to all caps"""
        self.content = self.content.upper()
        print(self.content)

    def __iter__(self):
        self.phrase_iterator = iter(self.content)
        return self

    def __next__(self):
        return next(self.phrase_iterator)

    def letters_and_digits(self):
        """Return the letters in the content."""
        return "".join(re.findall(r"[a-zA-Z\d]", self.content))


class TranslatedPhrase(Phrase):
    """A class to represent phrases with translation"""
    def __init__(self, content, translation):
        super().__init__(content)
        self.translation = translation
    def _processed_content(self):
        """Override superclass method to use translation"""
        return self.translation.lower()
    def __iter__(self):
        self.phrase_iterator = iter(self.translation)
        return self


def reverse(string):
    """Reverse a string"""
    return "".join(reversed(string))
