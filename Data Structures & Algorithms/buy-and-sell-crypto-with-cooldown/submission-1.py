class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ## cache
        dp = {} #  (i, buying) : max profit 

        def dfs(i, buying):
            """ buying (boolean) : If we are buying or selling """
            # Basecase:
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i,buying)]

            # If current state was buying, we would either sell or cooldown
            if buying:
                sell = dfs(i+1, not buying) - prices[i] #subtract the price at which we bought
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(sell, cooldown)

            # If the current state was selling, then we can either buy after cooldown or cooldown
            else:
                buy = dfs(i+2, not buying) + prices[i] # Add the profit we earned after selling
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)

     



        

        