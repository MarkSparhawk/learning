from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cnt = [0] * (n + 1)
        for item in citations:
            cnt[min(n,item)] += 1
        
        k = n
        s = cnt[k]
        print(cnt)
        while s < k and k >= 0:
            print(f"Start: {s=} {k=}")
            k -= 1
            s += cnt[k]
            print(f"End: {s=} {k=}")
        
        return k


    def hIndexold(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        
        i = 0
        while i < len(citations) and citations[i] > i:
            i += 1

        return i
    

def test_hindex():
    s = Solution()

    input = [3,0,6,1,5]
    want = 3
    assert s.hIndex(input) == want


    input = [1,3,1]
    want = 1
    assert s.hIndex(input) == want
