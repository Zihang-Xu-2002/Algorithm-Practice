from typing import List
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = len(words)
        for word in words:
            for i in word:
                if i not in allowed:
                    counter -= 1
                    break
        return counter