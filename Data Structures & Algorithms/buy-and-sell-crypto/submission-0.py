class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.l = 0
        self.r = 1
        self.profit = 0
        while self.r < len(prices):
            ## Check if buying price is lesser than selling price. If so, update the profit
            if prices[self.l] < prices[self.r]:
                profit = prices[self.r] - prices[self.l]
                self.profit = max(self.profit, profit)
            else : 
                self.l = self.r
            self.r +=1
        return self.profit


        