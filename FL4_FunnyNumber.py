#Funny Number

'''
    Problem : Duda is a very funny guy and recently found a new kind of numbers.
              He calls those numbers as funny numbers. Duda says that a funny
              numbers are numbers which hae prime number of prime factors.
              For example : prime factors of number 6 are 3 and 2, so 6 has 2 prime
              factors and 2 is a prime number, then 6 is a funny number. Similarly prime
              factors of number 8 is 2, so 8 has only one prime number, hence 8 is not a
              funny number.
              Now Duda, wants to determine whether a given number N is funny or not. Write a program
              to help Duda.
    
    Input : The first line of input contains T, number of testcases.
            Each testcase contains single line containing integer N, number given by Duda
    
    Output : For each testcase print "Funny" (without quotes) if the number given in that testcase
             given in that testcase is Funny, else print "Not Funny".
    
    Constraints : 1 <= T <= 1000
                  1 <= N <= 1000000
    
    Sample Input : 5
                   6
                   8
                   7
                   30
                   210
    
    Sample Output : Funny
                    Not Funny
                    Not Funny
                    Funny
                    Not Funny
'''

def getPrimeFactors(n):
    prime_factors = []
    
    # first step : get the prime factor 2 and repeat
    # the process till 2 is no longer a divisor of n
    while(n%2 == 0):
        # whenever the number is a multiple of 2
        # add 2 to the list of prime factors
        # in fact 2 is a prime number
        prime_factors.append(2)
        n = n // 2
    
    # second step : get the rest of the prime factors by starting with 3
    # repeat the process by incrementing the prime foctor by 2
    # till the square root of n is reached
    max_nb = int(pow(n,0.5))
    for pf in range(3,max_nb+1,2):
        while(n%pf == 0):
            prime_factors.append(pf)
            n //= pf
    
    # at the end of the previous iteration, the value of n is either
    # 0 or greater than 2 ; in the latter case, the corresponding value
    # is added to the list of the prime factors of initial n
    if n>2:
        prime_factors.append(n)
    
    return(sorted(prime_factors))


def isPrimeNumber(n):
    isPrime = 0
    nb_iter_max = int(pow(n,0.5))
    
    if (n>1):
        isPrime = 1
        for nb in range(2,nb_iter_max+1):
            if (n%nb == 0):
                isPrime = 0
                break
    
    return (isPrime == 1)

def isFunnyNumber(n):
    # get the number of the list of unique prime factors of n
    # for instance, if n=8, the list of the prime factors is :
    # [2, 2, 2], so the only prime factor is 2
    # if n=6, the list of the prime factors is :
    # [2, 3], so there are 2 distincts numbers in this list
    nb_prime = len(list(set(getPrimeFactors(n))))
    if isPrimeNumber(nb_prime):
        print("Funny", end="\n")
    else:
        print("Not Funny")

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        #print("the number is", int(input()),end="\n")
        isFunnyNumber(int(input()))
