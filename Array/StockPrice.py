prices = [7,1,5,3,6,4]

minPrice = float("inf")
maxProfit = 0

for i in range(len(prices)):
    if prices[i] < minPrice:
        minPrice = prices[i]
    elif prices[i] - minPrice > maxProfit:
        maxProfit = prices[i] - minPrice

print(maxProfit)