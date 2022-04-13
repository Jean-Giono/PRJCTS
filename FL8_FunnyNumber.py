# Funny Number

'''
    Problem : We call a positive integer a funny number, if it consists only of digits
              5 and 6 when written down in the usual way in the decimal system. We can
              enumerate all funny integers starting from the smallest one, i.e, : 5,6,55,56,65,etc.
                
              For a givenn number k, calculate the value of the k-th funny number in the sequence.
	
    
	Input : The input consists of a single positive integer k.
    
    
    Output : The value of the k-th smallest funny number.
    
    
    Constraint : 1 <= k <= 1000000000
    
    
    Sample Input 0 : 1
    Sample Input 1 : 10
    Sample Input 2 : 123456
    
    
    Sample Output 0 : 5
    Sample Output 1 : 566
    Sample Output 2 : 6665556556555556
'''

def getFunnyNumber(n):
    bin_n = bin(n+1)
    funny_nb = int(bin_n[3:].replace('0','5').replace('1','6'))
    return funny_nb


if __name__ == "__main__":
    k = int(input())
    funny_number = getFunnyNumber(k)
    print(funny_number, end="\n")