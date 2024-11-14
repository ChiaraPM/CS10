#This is lab13, short but there is no workbook.
#About recursion in Python


# Exercise 1
#This function will separate the digits 
#After dividing the numbers it will add them all 

#Use modular arithmetic to attain the last digit of a number
#Use floor division to strip the number of the last digit

def sum_digits(num: int) -> int:
    if num < 10: #can we also turn this to string and see if lenght of string is <=1?
        return num
    else:
        return (num%10) + sum_digits(num//10)
    
    """
    Separate each digit of the input and sum the digits together using recursion.

    Parameters:
    - num (int): The num to be recursively called

    Returns:
    int

    Examples:
    >>> sum_digits(1) 
    1
    >>> sum_digits(10) #returns 1 + 0
    1
    >>> sum_digits(111) #returns 1 + 1 + 1
    3
    >>> sum_digits(1234) #returns 1 + 2 + 3 + 4
    10
    >>> sum_digits(74219) #returns 7 + 4 + 2 + 1 + 9
    23
    """
    pass #

# Exercise 2
#In this exercise, make a function that finds the greatest common divisor

#a and b are both positive integers (not zero? or just positive?)
#We use modular arithmetic (%)
# % -> gives you the remainder after dividing the two numbers
# we work with model of (old number, remainder)
def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)
    """
    Calculate the greatest common divisor (GCD) of two positive integers using recursion.

    Parameters:
    - a (int): The first positive integer
    - b (int): The second positive integer

    Returns:
    int

    Examples:
    >>> gcd(48, 18) 
    6
    >>> gcd(54, 24) 
    6
    >>> gcd(101, 103) 
    1
    >>> gcd(56, 98) 
    14
    >>> gcd(100, 75) 
    25
    """
    pass #


# Exercise 3
#This function converts a non-negative integer to a binary representation
#Use the str function to output a string and not an integer

#Math way to go from Decimal to Binary; divide recursively by 2
#Remainders are then written in reverse order
#In the bits its 2 to the power of something // 8, 4, 2, 1
# // will give you the integer of the division result
# % will give us the reminder after dividing
# // 2 gives us the next bit
# %2 extracts the binary bit

def decimal_to_binary(n: int) -> str:
    if n <=1:
        return str(n)
    else:
        return str(decimal_to_binary(n//2)) + str(n%2)

    """
    Convert a non-negative integer to its binary representation using recursion.

    Parameters:
    - n (int): The non-negative integer to be converted

    Returns:
    str

    Examples:
    >>> decimal_to_binary(10)
    '1010'
    >>> decimal_to_binary(7)
    '111'
    >>> decimal_to_binary(0)
    '0'
    >>> decimal_to_binary(1)
    '1'
    >>> decimal_to_binary(20)
    '10100'
    """
    pass #




