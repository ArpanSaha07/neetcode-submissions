class Solution:
    def isValid(self, s: str) -> bool:

        # time complexity: O(n)
        # space complexity: O(n/2) -> O(n)

        hash_list = {")": "(", "}": "{", "]": "["}
        
        seen = []

        for c in s:

            if c in hash_list.keys():
                if len(seen) > 0 and hash_list[c] == seen[-1]:
                    seen.pop()
                else:
                    return False
            else:
                seen.append(c)

        return len(seen) == 0    


        