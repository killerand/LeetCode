class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)  # Create a default dictionary where each value is a list
        
        for s in strs:
            sorted_str = ''.join(sorted(s))  # Sort the string to form the key
            anagrams[sorted_str].append(s)  # Append the original string to the corresponding list in the dictionary
        
        return list(anagrams.values())  # Return the values of the dictionary as a list of lists
        