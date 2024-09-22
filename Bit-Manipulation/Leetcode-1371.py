class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # 用于记录元音对应的mask，a, e, i, o, u 对应的位分别是 0, 1, 2, 3, 4
        vowel_to_bit = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        
        mask = 0  # 初始mask是 00000，表示所有元音出现偶数次
        max_len = 0  # 记录最长子串长度
        first_occurrence = {0: -1}  # 记录每个mask第一次出现的位置，初始为 mask 0 出现在索引 -1
        
        for i, char in enumerate(s):
            # 如果字符是元音，更新 mask
            if char in vowel_to_bit:
                mask ^= vowel_to_bit[char]  # 翻转对应的元音位
            
            # 如果 mask 之前出现过，说明从之前到当前的元音出现次数是偶数
            if mask in first_occurrence:
                max_len = max(max_len, i - first_occurrence[mask])
            else:
                # 如果 mask 是第一次出现，记录其位置
                first_occurrence[mask] = i
        
        return max_len
