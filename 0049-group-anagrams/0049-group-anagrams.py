
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            # Sort characters to create key
            key = "".join(sorted(s))
            
            # Add original string to that key
            groups[key].append(s)

        return list(groups.values())