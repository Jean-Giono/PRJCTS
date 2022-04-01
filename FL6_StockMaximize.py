# Stock Maximize

'''
    Problem : Your algorithms have become so good at predicting the market that
               you now know what the share price of Wooden Orange Toothpicks Inc. (WOT) will be
               for the next number of days. 
               Each day, you can either buy one share of WOT, sell any number of shares of WOT that
               you own, or not make any transaction at all. What is the maximum profit you can 
               obtain with an optimum trading strategy ?
                
                Example :
                 * prices = [1,2] : buy one share day one, and sell it two for a profit of 1. Profit = 1.
                 * prices = [2,1] : no profit can be made so you do not buy or sell stock those days. Profit = 0.
                
                Write the function stockmax(prices), that returns the maximum profit achievable, given the prices.
                
    Input : prices is an array of integers that represent predicted daly stock prices.
    
    Output : an integer, that represent the maximum profit achievable.
    
    Input Format : The first line contains the number of test cases t.
                   Each of the next t pairs of lines contain:
                   - the first line contains an integer n, the number of predicted prices for WOT
                   - the next line contains n space-separated integers prices[i], each a predicted stock
                      price for day i.
    
    Constraints : 1 <= t <= 10
                  1 <= n <= 50000
                  1 <= prices[i] <= 100000
    
    Output format : Output t lines, each containing the maximum profit which can be obtained for corresponding test case.
    
    Sample Input : 3
                   3
                   5 3 2
                   3
                   1 2 100
                   4
                   1 3 1 2
   
    Sample Output : 0
                    197
                    3
    
'''

def stockmax(N, prices):
    shares = 0
    profit = 0
    m = max(prices)
    
    while len(prices) > 0:
        day = prices.pop(0)
        if day == m:
            profit += day*shares
            shares = 0
            if len(prices) > 0:
                m = max(prices)
        elif day < m:
            profit -= day
            shares += 1
    
    return profit


if __name__ == "__main__":
    
    for case in range(int(input())):
        N = int(input())
        prices = [int(x) for x in input().split()]
    
        print(stockmax(N, prices), end="\n")