def maxProfit(prices):
    maxProf = 0
    minBuy = prices[0]
    for price in prices:
        if(price < minBuy): # if new lowest price found, set it as new purchase price
            minBuy = price
        elif( minBuy-price > maxProf): # else if minBuy price < current price then set that difference to new maxProf
            maxProf = minBuy-price
    return maxProf