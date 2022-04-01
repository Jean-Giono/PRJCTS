# Vending Machine Report

'''
    Problem : A vending machine company needs to analyze how a particular machine
              is performing. To do so, they rely on two important pieces of data.
              The first is called a "check event", which indicates how many products
              were in the machine's inventory at the end of a certain day. The second
              is called a "fill event", which indicates how many products were added to
              the machine's inventory during the day (always before the "check event").
              Given the data logs for both these events, can you determine how many products
              were sold each day ?
              
              Note that in the data, days are numbered starting at 0. Also, the system records
              both the logs as pairs (day, parameter) without preserving the order in which they
              are written.
              
              For example, let's say checksEvents = [[1, 2], [0, 3]]. This means there were 2 inventory
              checks: on day 1, there were 2 products in the machine, and on day 0, there were 3
              products in the machine. Also, fillEvents = [[0, 5]], which means that there was a single
              event adding products to the inventory: on day 0, there 5 products added.
              
              Using this information, we can calculate that 2 products were sold on day 0 because 5
              products were added but only 3 were left at the end of the day. Then, 1 product was sold
              on day 1 - the day began with 3 products based on the previous day's data, but only  were
              left at the end of the day. Therefore, the answer is [2, 1] because that's how many products
              were sold each day.
              
              Write the function getReport, that must return an array of integers denoting how many
              products the machine sold each day.
    
    Input : checkEvents, a 2D integer array with n rows and 2 columns
            fillEvents, a 2D integer array with m rows and 2 columns
    
    Output : an array of integers that denotes how many products the machine sold
             each day
    
    Constraints : - 1 <= n, m <= 10^5
                  - 0 <= day < n, where day indicates the first column in checkEvents and fillEvents
                  - 0 <= k <= 1000, where k indicates the second column in checkEvents and fillEvents
                  - It is guaranted that the logs are valid (i.e., the number of products in the machine
                    never drops below 0, and no more products can appear in the inventory than were added there)
    
    Input Format : The first line contains an integer, n, denoting the number of rows in checkEvents.
                   The next line contains an integer, 2, denoting the number of columns in checkEvents.
                   Each line i of the n subsequent lines (where 0 <= i < n) contains two space-separated
                   integers, checkEvents[day][k], denoting the inventory of products at the end of each day.
                   The next line contains an integer, m, denoting the number of rows in fillEvents.
                   The next line contains an integer, 2, denoting the number of columns in fillEvents.
                   Each line i of the m subsequent lines (where 0 <= i < m) contains two space-separated integers,
                   fillEvents[day][k], denoting how many products were added to the inventory during each day.
                   
    Sample Input : 2
                   2
                   1 0
                   0 10
                   3
                   2
                   1 5
                   0 6
                   0 5
    
    Sample Output : 1
                    15
    
'''

def getReport(checkEvents, fillEvents):
    eventsMap = {} # day -> [checkEv, fillEv]
    
    for [day,evt] in checkEvents:
        eventsMap[day] = [evt]
    
    for [day,evt] in fillEvents:
        if len(eventsMap[day]) == 1:
            eventsMap[day].append(0)
        eventsMap[day][1] += evt
    
    len_events = len(eventsMap)
    sales = []
    
    for day in range(len_events):
        nb_remain = eventsMap[day][0]
        if len(eventsMap[day]) == 1:
            if day == 0:
                sales.append(0)
            else:
                sales.append(eventsMap[day-1][0] - nb_remain)
        else:
            if day == 0:
                sales.append(eventsMap[day][1] - nb_remain)
            else:
                sales.append(eventsMap[day-1][0] + eventsMap[day][1] - nb_remain)
    return sales


if __name__ == '__main__':
    checkEvents_rows = int(input())
    checkEvents_columns = int(input())
    
    checkEvents = []
    
    for _ in range(checkEvents_rows):
        checkEvents.append(list(map(int, input().split())))
    
    fillEvents_rows = int(input())
    fillEvents_columns = int(input())
    
    fillEvents = []
    
    for _ in range(fillEvents_rows):
        fillEvents.append(list(map(int, input().split())))
    
    result = getReport(checkEvents, fillEvents)
    
    print(' '.join(map(str,result)), end="\n")