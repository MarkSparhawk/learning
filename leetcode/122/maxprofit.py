from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        result = 0
        trade = 0
        buy = 0
        sell = 1

        while sell < len(prices):
            
            # evaluate trade
            if prices[sell] > prices[buy]:
                if prices[sell] - prices[buy] > trade:
                    trade = prices[sell] - prices[buy]
                else:
                    result = result + trade
                    trade = 0
                    buy = sell
                    sell = sell +1
            else:
                buy += 1
                sell += 1

        return result



def test_maxProfit():
    s = Solution()

    input = [7,1,5,3,6,4]
    want = 7
    assert s.maxProfit(input) == want

    input = [7,1,5,3,7,4]
    want = 8
    assert s.maxProfit(input) == want

    input = [1,2,3,4,5]
    want = 4
    assert s.maxProfit(input) == want

    input = [7,6,4,3,1]
    want = 0
    assert s.maxProfit(input) == want
