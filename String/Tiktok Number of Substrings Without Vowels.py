#https://www.fastprep.io/problems/tiktok-number-of-substrings-without-vowels

class Solution:
  def numberOfSubstringsWithoutVowels(self, s: str) -> int:
    voewls = {'a', 'e', 'i', 'o', 'u'}
    substrings = []
    # 外层循环用于起点
    for i in range(len(s)):
        # 内层循环用于终点
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    subStringToRemove = []
    for item in substrings:
        if any(c in voewls for c in item):
            subStringToRemove.append(item)
    for item in subStringToRemove:
        substrings.remove(item)
    return len(substrings)

s = "abc"
solution = Solution()
print(solution.numberOfSubstringsWithoutVowels(s)) # 3