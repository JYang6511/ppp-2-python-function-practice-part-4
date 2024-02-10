'''
Write a Python function called max_num()to find the maximum of three numbers.
Write a Python function called mult_list() to multiply all the numbers in a list.
Write a Python function called rev_string() to reverse a string.
Write a Python function called num_within() to check whether a number falls in a given range.
The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
The function accepts the number n, the number of rows to print
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
'''
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
    



