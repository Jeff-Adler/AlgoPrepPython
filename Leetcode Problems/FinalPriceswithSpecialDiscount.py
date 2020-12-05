# Restatement: For every element in prices, i represents the item, prices[i] represents the cost of that time. Return an array that meets the following condition: for every element in prices[i], find the minimum/lowest index, j, such that j is greater than i, and prices[j] is less than or equal to prices[i]. In other words, for each element in prices, find the next item in the list that is greater than or equal to that element. Then, return the price of i minus the prices of elements j that meets the condition

# Approach: simply make a condition that checks if condition holds
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        discounted_prices = []

        while len(prices) - 1:
            item1 = prices.pop(0)

            item2 = next((price for price in prices if price <= item1), 0)

            discounted_prices.append(item1 - item2)

        discounted_prices.append(prices[0])

        return discounted_prices


# class Solution:
#     def finalPrices(self, prices: List[int]) -> List[int]:
#         discounted_prices = []

#         def is_less_than(item1, item2):
#             return item2 <= item1

#         def apply_discount(item1, item2):
#             return item1 - item2

#         while (len(prices) - 1):
#             item = prices.pop(0)
#             if min(prices) > item:
#                 discounted_prices.append(item)
#             else:
#                 j = 0
#                 while j < len(prices):
#                     if is_less_than(item, prices[j]):
#                         discounted_prices.append(
#                             apply_discount(item, prices[j]))
#                         break
#                     j += 1

#         discounted_prices.append(prices[0])

#         return discounted_prices
