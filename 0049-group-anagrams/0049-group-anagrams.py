from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tot_dict = {}
        for i in strs:
            cnt = [0] * 26
            for j in i:
                cnt[ord(j) - ord('a')] += 1
            if tuple(cnt) not in tot_dict:
                tot_dict[tuple(cnt)] = [i]
            else:
                tot_dict[tuple(cnt)].append(i)
        return tot_dict.values()







        