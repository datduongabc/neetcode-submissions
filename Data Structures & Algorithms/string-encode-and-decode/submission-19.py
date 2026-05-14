class Solution:

    def encode(self, strs: List[str]) -> str:
        sender = ""
        
        for word in strs:
            sender += str(len(word)) + "#" + word
        return sender

    def decode(self, s: str) -> List[str]:
        receiver = []

        letter_idx = 0
        while letter_idx < len(s):
            str_length = ""
            while '0' <= s[letter_idx] <= '9':
                str_length += s[letter_idx]
                letter_idx += 1
            length = int(str_length)

            if s[letter_idx] == '#':
                letter_idx += 1
                receiver.append(s[letter_idx: letter_idx + length])
                letter_idx += length

        return receiver