class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""

        for word in strs:
            new_str += str(len(word)) + "#" + word

        return new_str

    def decode(self, s: str) -> List[str]:
        cursor = 0
        word = ""
        LengthOfWord = ""
        LIST = []

        while cursor < len(s):
            while s[cursor] != "#":
                LengthOfWord += s[cursor]
                cursor += 1

            cursor += 1

            while len(word) < int(LengthOfWord):
                word += s[cursor]
                cursor += 1

            LIST.append(word)
            word = ""
            LengthOfWord = ""

        return LIST