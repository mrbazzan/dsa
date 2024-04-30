
from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoding_str = ""
        for i in strs:
            encoding_str += str(len(i)) + '#' + i
        return encoding_str

    def decode(self, string: str) -> List[str]:
        i = 0
        length = 0
        decoding_list = []
        while i < len(string):
            i += 1
            if string[i] != '#':
                continue

            length = int(string[length:i]) + i + 1
            decoding_list.append(
                string[i+1:length]
            )
            i = length

        return decoding_list


# encode method -> "lint:;code:;love:;you"

encoded = Solution().encode(["l8#nt", "co2e", "lovedjidru4", "you"])
solution = Solution().decode(encoded)
print(solution)

