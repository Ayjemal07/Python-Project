""" Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. """

def hello_name(user_name):
    print("hello_"+ user_name.upper()+"!")

""" Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing """

def first_odds():
    for num in range(100):
        if num%2!=0:
            print(num)

""" Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. """

def max_num_in_list(a_list):
    return max(a_list)

""" Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false). """

def is_leap_year(a_year):
    if (a_year%4==0 and a_year%100!=0) or (a_year%400==0):
        return True
    else:
        return False

""" Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type """

def is_consecutive(a_list):
    first_num=a_list[0]
    for num in a_list[1:]:
        if num-first_num==1:
            it_is=True
            first_num=num
        else:
            it_is=False
    return it_is

