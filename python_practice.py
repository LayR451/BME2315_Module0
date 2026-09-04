# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

# No generative AI was used in the making of this code

# Heading
# Name: Layla Ragland 


# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments
First, set 2 variables to the first 2 digits of Fibonacci (a and b)
Set a count and a total
Define a variable as the interger value of the number of terms you want in your sequence (N)

While the count is less than the N,
      The total adds b
      The next value is set as the sum of a and b
      We need a new a, make it the old b
      And now b is the next value we created
      add to the count to show a cycle has been completed
      exit 



"""
# MY NAME IS LAYLA
# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 # The count is set to 0
total = 0 # Total sum set to 0

while count < (N-1):  # Because we start with a and b terms, we only need 5 more cycles, so less than n-1
    total = total + b  # adding up the newest term to the totla
    next_value = a + b   # defining the next term
    a = b              # resetting the new a value
    b = next_value     # resetting the new b value 
    count = count + 1  # updating our count 

# cycling through while loop until count is > N-1

print(total)   # printing our final answer

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.
'''
Strategy: Use above Fibonnaci sequence loop to feed into a list, and then run it on that list
'''
import numpy as np
N = 10

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 # The count is set to 0
total = 0 # Total sum set to 0
f_sequence = [0]

while count < (N-1):  # Because we start with a and b terms, we only need 5 more cycles, so less than n-1
    f_sequence.append(b)
    total = total + b  # adding up the newest term to the totla
    next_value = a + b   # defining the next term
    a = b              # resetting the new a value
    b = next_value     # resetting the new b value 
    count = count + 1  # updating our count 

std_dev = np.std(f_sequence)
print(f_sequence, 'has a standard deviation of', std_dev)


# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.


def fibonacci(N):
        
    a = 0 # set a to the first fibonacci number
    b = 1 # set b to the second fibonacci number
    count = 0 # The count is set to 0
    total = 0 # Total sum set to 0

    while count < (N-1):  # Because we start with a and b terms, we only need 5 more cycles, so less than n-1
        total = total + b  # adding up the newest term to the totla
        next_value = a + b   # defining the next term
        a = b              # resetting the new a value
        b = next_value     # resetting the new b value 
        count = count + 1  # updating our count 

    return total

totals_list = [0]

for N in [5, 10, 15, 20, 25, 30]:
    a = fibonacci(N)
    totals_list.append(a)

print(totals_list)


# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit): 
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    limit = int(limit)  
    a = 0
    b = 1
    index = 0

    while a <= limit:   # A typeError, meaning wrong use of operator/category, due to a <= between a str and int. I fixed it by making a and b ints, not strings. Then, a NameError because limit was not defined well, so I made a line to ensure Limit was always int and wouldn't cause an edge case error.
        next_value = a + b
        a = b
        b = next_value
        index += 1   # UnboundLocalError because index isn't defined outside of the function. So, I defined it outside of the function.

    return index


result = find_fib_above_limit(50)
print("The index of the first number above your limit is: ", result)



# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. 
# The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_odd_fib(limit):
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 != 0:
            total += b
        a, b = b, a + b
    return total


# Add your test cases here
sum_odd_fib(3)
sum_odd_fib(5)
sum_odd_fib(7)



# %%
