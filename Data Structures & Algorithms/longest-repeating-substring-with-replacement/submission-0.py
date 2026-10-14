class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Time complexity: O(26n) -> O(m * n) -> O(n)
        # Space complexity: O(26) -> O(1) -> O(m)
        # Where n is the length of the string and m is the total number of unique characters in the string.

        # Misc notes:
        # (n - 1) + (n - 2) + ... + 1 = n(n - 1) / 2 = O(n²)
        # length - maxfreq <= k
        # ABAABBA

        char_freq = {}
        result = 0

        left = 0

        for right in range(len(s)):

            char = s[right]

            char_freq[char] = char_freq.get(char, 0) + 1

            while (right - left + 1) - max(char_freq.values()) > k:
                char_freq[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
            


                






            



