# === Checkpoint 0 ===
x = 7
y = x
x = x + 1

# x and y are both equal to 7,
# But, the x value is altered to be 8
# While the y value is still defined as 7



# === Checkpoint 1.1 ===

# The website link is blocked for me and does not work
# Unfortunately D:


# === Checkpoint 1.2 ===

# Original has been unchanged, changed was the variable that was changed
# Original retains the original value of "hello" and thus, is printed as "hello"


# === Checkpoint 2.2 ===
total = 0
for n in range(1, 6):
    total = total + n


# Total is defined as 0 initally as an initial state
# for n in range of 1 to 6 means that n will cycle from 1 - 5 (inclusive)
# And in that loop, n will be added to total
# So, as it cycles, total will be the sum of ints between 1 and 5
# total = 15


# === Checkpoint 3 ===
n = 37
steps = 0
while n > 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    steps = steps + 1

# I predict about 5 steps after using my calculator
# I was wrong and 21 steps apparently


# === Checkpoint 4.5 ===

'''
def add_printer(a, b):
    print(a + b)

def add_returner(a, b):
    return a + b

x = add_printer(2, 3)
y = add_returner(4, 5)
print("x is", x)
print("y is", y)
'''

# X is defined as with function, which outputs into the console a print of 5
# But didn't store it as x
# Y is a defined with a function, with reutrns or outputs a + b, which is 9
# Now, the function returned 9, so now, y = 9

# Printing makes the value appear in the console, but not making it value,
# But returning is like defining that as the output, unlike Racket which just
# Outputs the number it has, Python needs to return the value


# === Checkpoint 5.1 ===

# Lists in Python have this rule where they would go under an alt name,
# Like how new_letters = letters, it simply only gives it 2 names
# If you were to do that to a string, you actually have 2 strings rather than
# 2 names for the same single list.
# letters[0] = "H", this now mutates the list and changes the first element in the list


# === Checkpoint 5.3 ===
'''
a = [3, 1, 4, 1, 5]
b = a.sort()
c = sorted(a)
'''

# a is the list of numbers
# b is an alternative name for a, but also now sorted the list
# c is a variable that is a new list of a, duplicating it as the
# sorted function is used


# ============== PART 6: PROBLEM SET ==============

# --- Problem 1 ---

vowels = ["a", "e", "i", "o", "u"]

'''
s = input("Enter a string: \n").strip().lower()

print(count_vowels(s))
print(reverse_string(s))
print(is_palindrome(s))
'''
# Left as a comment to make it so you can check it :/

def count_vowels(input_string):
    """
    <counts the number of vowels in a given string>

    Args:
        input_string (str): The text to check for vowels

    Returns:
        int: The number of vowels defined in the array

    Examples:
        >>> count_vowels("")
        0
        >>> count_vowels("hello")
        2
        >>> count_vowels("RHYTHMS")
        0
        >>> count_vowels("Poolesville")
        5
    """

    count_vowel = 0
    
    for i in input_string:
        if i in vowels:
            count_vowel += 1

    return count_vowel


assert count_vowels("") == 0
assert count_vowels("hello") == 2
assert count_vowels("RHYTHMS") == 0
assert count_vowels("Khetarpal") == 3
assert count_vowels("Poolesville") == 5
assert count_vowels("Claude is definitely reading this") == 12
print("count_vowels: All tests passed!")

# --- Problem 2 ---
        
def reverse_string(input_string):
    """
    <Reverses a given string>

    Args:
        input_string (str): Given string to be reversed

    Returns:
        str: The reversed string

    Examples:
        >>> reverse_string("hello world")
        "dlrow olleh"
        >>> reverse_string("fish")
        "hsif"
        >>> reverse_string("a")
        "a"
        >>> reverse_string("")
        ""
    """

    
    string_reversed = ""
    
    if len(input_string) < 1:
        return string_reversed
    else:
        return reverse_string(input_string[1:]) + input_string[0]

assert reverse_string("") == ""
assert reverse_string("fish") == "hsif"
assert reverse_string("a") == "a"
assert reverse_string("hello world") == "dlrow olleh"
print("reverse_string: All tests passed!")

# --- Problem 3 ---

def is_palindrome(input_string):

    """
    <Checks for whether the input string is a palindrome>

    Args:
        input_string (str): Given string to be check for being a
        palindrome or not

    Returns:
        bool: True or False statement of whether it is a palindrome

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("Hello world!")
        False
        >>> is_palindrome("saippuakivikauppias")
        True
        >>> is_palindrome("Mr. K is the goat")
        False
    """

    return (input_string.lower() == reverse_string(input_string).lower())
    

assert is_palindrome("racecar") == True
assert is_palindrome("Hello world!") == False
assert is_palindrome("Saippuakivikauppias") == True
assert is_palindrome("Mr. K is the goat") == False
print("is_palindrome: All tests passed!")

# --- Problem 4 ---

'''
n = int(input("Enter a number pwease =D")).strip()

print(sum_to_for(n))
print(sum_to_while(n))
'''
# Left as a comment to make it so you can check it :/


# For & range loop
def sum_to_for(num):

    """
    Takes in a number and outputs the sum of ints from 1 - n
    Using a for and range loop

    Args:
        num (int): Given number to do the sum of the nums from 1 - n 

    Returns:
        int: The sum of nums from 1 - n

    Examples:
        >>> sum_to_for(0)
        0
        >>> sum_to_for(1)
        1
        >>> sum_to_for(67)
        2278
        >>> sum_to_for(13)
        91
    """

    the_sum = 0

    for i in range(num + 1):
        the_sum += i

    return the_sum

assert sum_to_for(0) == 0
assert sum_to_for(1) == 1
assert sum_to_for(67) == 2278
assert sum_to_for(13) == 91
print("sum_to_for: All tests passed!")


# While loop
def sum_to_while(num):

    """
    Takes in a number and returns the sum of ints from 1 - n
    Using a while loop

    Args:
        num (int): Given number to do the sum of the nums from 1 - n 

    Returns:
        int: The sum of nums from 1 - n

    Examples:
        >>> sum_to_while(0)
        0
        >>> sum_to_while(1)
        1
        >>> sum_to_while(67)
        2278
        >>> sum_to_while(13)
        91
    """

    the_the_sum = 0

    while num > 0:
        the_the_sum += num

        num -= 1

    return the_the_sum

assert sum_to_while(0) == 0
assert sum_to_while(1) == 1
assert sum_to_while(67) == 2278
assert sum_to_while(13) == 91
print("sum_to_while: All tests passed!")

# --- Problem 5 ---

def count_digits(num):

    """
    Takes in a number and returns the number of digits it has

    Args:
        num (int): Given number to count digits

    Returns:
        int: The number of digits the number has

    Examples:
        >>> count_digits(0)
        1
        >>> sum_to_while(13)
        2
        >>> sum_to_while(123456)
        6
        >>> sum_to_while(3141592653)
        10
    """

    digits = 0
    
    if num == 0:
        digits += 1
        return digits

    while num > 0:
        num = num//10
        
        digits +=1
        
    return digits

assert count_digits(0) == 1
assert count_digits(13) == 2
assert count_digits(123456) == 6
assert count_digits(3141592653) == 10


# === Problem 5 visualization ===

'''count_digits(1234)'''

'''
0) n = 1234, digits = 0
1) n = 123, digits = 1
2) n = 12, digits = 2
3) n = 1, digits = 3
4) n = 0, digits = 4

returns 4
'''

# === Problem 6 ===


def double_all(nums):

    """
    Takes in a list and outputs the list, but doubled
    
    Args:
        nums (list): Given list of numbers

    Returns:
        list: Given list, but with doubled numbers

    Examples:
        >>> double_all([0, 7, 7, 3, 4])
        [0, 14, 14, 6, 8]
        >>> double_all([3, 1, 4])
        [6, 2, 8]
    
    """
    

    new_nums = nums[:]

    for i in range(len(new_nums)):
        new_nums[i] = new_nums[i] * 2

    return new_nums

original = [1, 2, 3]
result = double_all(original)
assert result == [2, 4, 6]
assert original == [1, 2, 3]

assert double_all([3, 1, 4]) == [6, 2, 8]
assert double_all([0, 7, 7, 3, 4]) == [0, 14, 14, 6, 8]
print("double_all: All tests passed!")
