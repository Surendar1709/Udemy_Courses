'''"Problem Description: You are given an integer n. Your task is to return a square pattern of size n x n made up of the character '*', represented as a list of strings."
""
"Input Parameters:
n (int): The size of the square (number of rows and columns).



Output:

A list of strings where each string is a row of n characters.



Example:

Input: 3
Output: ['***', '***', '***']
 
Input: 5
Output: ['*****', '*****', '*****', '*****', '*****']" '''

def squearelist(n):
    result=[]
    for i in range(n):
        result.append("*"*n)
    return result

n=5
final_result=squearelist(n)
print(final_result)

''' Hollow Square of side 'N'
Problem Description:

You are given an integer n. Your task is to return a hollow square pattern of size n x n made up of the character '*', represented as a list of strings. The hollow square has '*' on the border, and spaces ' ' in the middle (except for side lengths of 1 and 2).



Input Parameters:

n (int): The size of the square (number of rows and columns).


Output:

A list of strings where each string is a row of n characters, representing a hollow square.



Example:

Input: 3
Output: ['***', '* *', '***']
 
Input: 5
Output: ['*****', '*   *', '*   *', '*   *', '*****']'''

def HollowSquare(n):
    l1=[]
    if n==1:
        return["*"]
    l1.append("*"*n)
    for i in range(n-2):
        l1.append("*"+" "*(n-2)+"*")

    l1.append("*"*n)
    return l1

n=5
r=HollowSquare(n)
print(r)

'''Rectangle Pattern
Problem Description:

You are given two integers, n and m. Your task is to return a rectangle pattern of '*', where n represents the number of rows (length) and m represents the number of columns (breadth).



Input:

Two integers n and m, where 1 <= n, m <= 100.



Output:

A list of strings where each string represents a row of the rectangle pattern.



Example:

Input: n = 4, m = 5
Output: ['*****', '*****', '*****', '*****']
 
Input: n = 3, m = 2
Output: ['**', '**', '**']'''

def  Rectangle_Pattern(n,m):
    l1=[]
    for i in range(n):
        l1.append("*"*m)
    return l1
n,m=4,5
r=Rectangle_Pattern(n,m)
print(r)


"""Right Angled Triangle
Problem Description:

You are given an integer n. Your task is to return a right-angled triangle pattern of '*' where each side has n characters, represented as a list of strings. The triangle has '*' characters, starting with 1 star in the first row, 2 stars in the second row, and so on until the last row has n stars.



Input Parameters:

n (int): The height and base of the right-angled triangle.



Output:

A list of strings where each string is a row of '*' characters that increases in length from 1 to n.



Example:

Input: 3
Output: ['*', '**', '***']
 
Input: 5
Output: ['*', '**', '***', '****', '*****']
"""
def right_angle(n):
    pattern=[]
    for i in range(1,n+1):
        pattern.append("*"*i)
    return pattern

n=5
result=right_angle(n)
print(result)

'''You are given an integer n. Your task is to return an inverted right-angled triangle pattern of '*' where each side has n characters, represented as a list of strings. The first row should have n stars, the second row n-1 stars, and so on, until the last row has 1 star.



Input Parameters:

n (int): The height and base of the inverted right-angled triangle.



Output:

A list of strings where each string is a row of '*' characters that decreases in length from n to 1.



Example:

Input: 3
Output: ['***', '**', '*']
 
Input: 5
Output: ['*****', '****', '***', '**', '*']'''

def invertedtriangle(n):
    l1=[]
    for i in range(n,0,-1):
        l1.append("*"*i)

    return l1
n=5
r=invertedtriangle(n)
print(r)

'''
Pyramid Pattern
Problem Description:

You are given an integer n. Your task is to return a pyramid pattern of '*' where each side has n rows, represented as a list of strings. The pyramid is centered, with 1 star in the first row, 3 stars in the second row, and so on, increasing by 2 stars per row until the base row has 2n - 1 stars.



Input:

A single integer n, where 1 <= n <= 100.



Output:

A list of strings where each string contains stars ('*') centered, forming a pyramid shape. Each row has an increasing number of stars, with appropriate spaces for centering.



Example:

Input: 3
Output: ['  *  ', ' *** ', '*****']
 
Input: 5
Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********']
'''

def center_triangle(n):
    l1=[]
    for i in range(1,n+1):
        space=" "*(n-i)
        star="*"*(2*i-1)
        l1.append(space+star+space)
    return l1
n=5
r=center_triangle(n)
print(r)

'''Inverted Pyramid Pattern
Problem Description

You are given an integer n. Your task is to return an inverted pyramid pattern of '*', where each side has n rows, represented as a list of strings. The first row has 2n - 1 stars, the second row has 2n - 3 stars, and so on, until the last row has 1 star, with each row centered using spaces.



Input Parameters:

n (int): The number of rows in the inverted pyramid.



Output:

A list of strings where each string represents a row of the inverted pyramid.


Example:

Input: 3
Output: ['*****', ' *** ', '  *  ']
 
Input: 5
Output: ['*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']
'''

def inverted_pyramid(n):
    lis = []
    for i in range(n):
        space = " " * i
        star = "*" * (2*(n - i) - 1)
        lis.append(space + star + space)
    return lis

n = 5
r = inverted_pyramid(n)
print(r)
