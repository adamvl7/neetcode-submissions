class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for words in strs:
            label = "".join(sorted(words))

            if label not in groups:
                groups[label] = []
            
            groups[label].append(words)
        
        return list(groups.values())

