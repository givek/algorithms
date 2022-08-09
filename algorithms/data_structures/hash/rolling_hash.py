class RollingHash:
    def __init__(self, word, alpha_size=256):
        self.word = word
        self.alpha_size = alpha_size  # total chars = 256 (ASCII)
        self.word_hash = self.hash_word(word)

    def hash_word(self, word):
        final_hash = 0

        for i, char in enumerate(reversed(word)):
            final_hash += ord(char) * (self.alpha_size**i)

        return final_hash

    def append(self, char):
        if not len(char) == 1:
            return  # cannot append more than 1 char

        self.word += char
        self.word_hash *= self.alpha_size
        self.word_hash += ord(char)

    def skip(self):

        first_char = self.word[0]
        self.word = self.word[1:]

        self.word_hash -= ord(first_char) * (self.alpha_size ** len(self.word))


def main():
    word = "henlo"

    r_word = RollingHash(word)

    r_word.append("g")
    r_word.append(" ")

    r_word.skip()

    r_word.append("y")
    r_word.append("x")

    r_word.skip()
    r_word.skip()

    print(r_word.word_hash)


if __name__ == "__main__":
    main()
