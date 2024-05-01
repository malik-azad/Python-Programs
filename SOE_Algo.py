#SIEVE OF ERATOSTHENES ALGORITHM

# he sieve of Eratosthenes algorithm is an ancient algorithm that is used to find all the prime numbers less than given number T. It can be done using O(n*log(log(n))) operations. Using this algorithm we can eliminate all the numbers which are not prime and those that are less than given T. Also, we will traverse from 2 to the root of the given number ( √T ).

# REASON FOR TRAVERSING UNTIL ( √T )
# There will not exist any factor of T greater than ( √T ). Suppose x and y are the factors of T. In that case, x*y = T . Hence, at least one or both should be <=√ T, so we need to traverse until ( <=√ T ) only.

# Define a function named 'prime_eratosthenes' that generates prime numbers using the Sieve of Eratosthenes algorithm
def prime_eratosthenes(n):
    prime_list = []  # Create an empty list to store prime numbers
    # Iterate through the numbers from 2 to 'n'
    for i in range(2, n+1):
        if i not in prime_list:
            # If 'i' is not in the 'prime_list,' it's a prime number; print it
            print(i)

            # Mark all multiples of 'i' as non-prime by adding them to 'prime_list'
            for j in range(i*i, n+1, i):
                prime_list.append(j)

# Call the 'prime_eratosthenes' function with 'n' set to 100 to generate prime numbers
# The function does not have a return value, so it prints the prime numbers directly
prime_eratosthenes(100)