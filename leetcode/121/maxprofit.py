from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        result = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                result = max(result, prices[j] - prices[i])
                    

        return result



def test_maxProfit():
    s = Solution()

    input = [7,1,5,3,6,4]
    want = 5
    assert s.maxProfit(input) == want

    input = [7,1,5,3,7,4]
    want = 6
    assert s.maxProfit(input) == want