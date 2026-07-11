class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        # max_profit=0
        # for i in range(n):
        #     buy=prices[i]
        #     for j in range(i+1,n):
        #         sell=prices[j]
        #         max_profit=max(sell - buy, max_profit)
        # return max_profit          

        l,r=0,1
        max_profit=0
        while r < n:
            if prices[l] < prices[r]:
                max_profit=max(max_profit, prices[r]-prices[l])
            else:
                l=r
            r+=1
        return max_profit            


