
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices)-1):
            max_price = max(prices[i+1:])
            profit = max(profit, max_price-prices[i])

        return profit

print(Solution().maxProfit([7,1,5,3,6,4]))  # 7 4 5 3 1 6  # 6 7 4 5 2 1 8 5
print(Solution().maxProfit([2,1,4]))
print(Solution().maxProfit([7,6,4,3,1]))
