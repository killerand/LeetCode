from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        # Initialize variables
        word_len = len(words[0])
        word_count = len(words)
        substring_len = word_len * word_count
        s_len = len(s)

        # Early return if s is too short to contain the concatenation of all words
        if s_len < substring_len:
            return []

        # Count the frequency of each word in words
        word_freq = Counter(words)

        # Result list to store starting indices
        result = []

        # Iterate over each possible starting point of the window
        for i in range(word_len):
            left = i
            right = i
            current_freq = Counter()

            # Slide the window over the string s
            while right + word_len <= s_len:
                word = s[right:right + word_len]
                right += word_len

                if word in word_freq:
                    current_freq[word] += 1

                    # If there are more occurrences of "word" than required, move the left pointer
                    while current_freq[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        current_freq[left_word] -= 1
                        left += word_len

                    # Check if we found a valid substring
                    if right - left == substring_len:
                        result.append(left)
                else:
                    # If the word is not in the given list, reset the window
                    current_freq.clear()
                    left = right

        return result