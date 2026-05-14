class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""

        for word in strs:
            new_str += "|"
            if word == "":
                new_str += "~"
            else:
                new_str += word

        return new_str

    def decode(self, s: str) -> List[str]:
        cursor = 0
        LIST = []
        word = ""

        while (cursor < len(s)):
            if (s[cursor] == "|"):
                cursor += 1
                continue

            if (s[cursor] == "~"):
                cursor += 1
                LIST.append("")
                continue
            
            while (cursor < len(s) and s[cursor] != "|"):
                word += s[cursor]
                cursor += 1

            LIST.append(word)
            word = ""

        return LIST