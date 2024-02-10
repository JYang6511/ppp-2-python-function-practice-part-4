# Write a Python function called max_num()to find the maximum of three numbers.

def max_num(a,b,c):
    return max(a, b, c)


print(max_num(11,33,4))


# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(list):
    result = 1
    for i in list:
        result *= i
    return result

my_list = [2, 3, 4, 10]
result = mult_list(my_list)
print(result)
    
# Write a Python function called rev_string() to reverse a string.

def rev_string(string):
    return string[::-1]

string = "Konichiwa"

reversed_string = rev_string(string)
print(reversed_string)


# Write a Python function called num_within() to check whether a number falls in a given range.


def num_within(num, rangebeg, rangeend):
    return rangebeg <= num <= rangeend

result = num_within(11, 2, 44)
print(result)


'''
Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
The function accepts the number n, the number of rows to print
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
'''
def pascal(n):   
    # Function to calculate binomial coefficient
    def binomial_coefficient(n, k):
        if k == 0 or k == n:
            return 1
        return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)
    
    # Loop to print each row of Pascal's triangle
    for i in range(n):
        # Print leading spaces to center the triangle
        print(" " * (n - i - 1), end="")
        
        # Print elements of the current row
        for j in range(i + 1):
            print(binomial_coefficient(i, j), end=" ")
        print()


pascal(2)
