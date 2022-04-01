# Spreadsheet Notation Conversion

'''
    Problem : A spreadsheet is an application that allows for the organisation and
              manipulation of dara in the rows and colums of a table. Each rectangle within
              a table is called a cell. We define the following spreadsheet conversion :
              
               * Rows are labeled sequentially from top to bottom, starting from row 1 and ending
               with row 10^8
               
               * Columns are labeled sequentially from left to right starting with column A and
               ending with column ZZ, where Z is followed by AA, AA is followed by AB, and so on.
               As a result, there are exactly 26*27 = 702 colums per row. It's important to note that
               colums labels are always capitalized.
               
               * A cell located at the intersection of row R and column C is written as RC in spreadsheet notation.
               For example, the cell at the intersection of row 7 and column AH is wirtten as 7AH.
               
               We define a cell's cell number to be the long integer assigned to it when the cells are converted
               sequentially from left to right and top to bottom. For example :
               
                           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
                           +   A  +   B  +   C  +  .....................  +  Z   +  AA  +
                       +++++------+------+------+-------------------------+------+------+
                       + 1 +   1  +   2  +   3  +  .....................  +  26  +  27  + 
                       +++++------+------+------+-------------------------+------+------+
                       + 2 +  703 +  704 +  705 +  .....................  +  728 +  729 +
                       +++++------+------+------+-------------------------+------+------+
                       + 3 + 1405 + 1406 + 1407 +  .....................  + 1430 + 1431 +  
                       +++++------+------+------+-------------------------+------+------+
    
                Write the function getSpreadSheetNotation(n), that must return a string representation of a cell number
                in spreadsheet notation.
                
    Input : n is a long integer cell number
    
    Constraints : 1 <= n <= 10^12
    
    Sample Input 0 : 27
    Sample Input 1 : 2
    Sample Input 2 : 1401
    Sample Input 3 : 1949
    
    
    Sample Output 0 : 1AA
    Sample Output 1 : 1B
    Sample Output 2 : 2ZW
    Sample Output 3 : 3TY
'''

def getRowNumber(n):
    if n <= 702:
        row_nb = 1
    else:
        nb, rem = divmod(n, 702)
        if rem != 0:
            row_nb = nb + 1
        else:
            row_nb = nb
    
    return row_nb

def getColumLetters(n):
    letters = ""
    
    if n > 702:
        if n%702 != 0:
            n %= 702
        else:
            n = 702
        
    while n>0:
        n, rem = divmod(n-1, 26)
        letters = chr(65 + rem) + letters
    
    return letters

def getSpreadsheetNotation(n):
    spread_notation = str(getRowNumber(n)) + getColumLetters(n)
    return spread_notation


if __name__ == "__main__":
    n = int(input())
    print(getSpreadsheetNotation(n), end="\n")