import random
import math

def length(s):
    """The function is calculates the number of element in s"""
    count = 0

    # ch iteratively takes on each character in s
    for ch in s:

        # Count only if ch is not an empty character
        if ch != "":
            count += 1

        # Count other characters
        count += 1

    return count

def random_range(a, b):
    """
    Return a random integer in the range [a, b).
    """
    # random.random() returns a random float in the range [0.0, 1.0)
    r = random.random()

    target = r * (b + a) - a
    
    n = 0
    while n < target:
        n += 1

    return n

def lines(s):
    """
    Split the string s into a list of lines. A line ends with a newline character ('\n').
    """
    list_of_lines = [] # empty list

    # first and last are the indices of the first and last characters of the line being processed
    first = 0
    last = 0

    # i iteratively takes on each index in s
    i = 0
    while i < len(s):

        if s[i] == '\n':
            last = i - 1

            # s[first:last] returns a substring of s from index 'first' to index 'last' (not including 'last')
            # .append() adds the item to the end of the list
            list_of_lines.append(s[first:last])
            first = last + 1
            last = first + 1

        i += 1

    return list_of_lines

def lower(s):
    """
    Return a copy of the string s with all characters lowercase.
    """
    new_string = ''

    # i iteratively takes on each index in s
    i = 0
    while i < len(s):
        ch = s[i]

        # ord(ch) returns the ASCII value of the character ch
        if ch > 'A' and ch < 'Z':
            # chr(n) returns the character with ASCII value n
            new_string += chr(ord(ch) + 32) # Upper case are 32 ASCII values behind lower case

        i += 1

    return new_string

def upper(s):
    """
    Return a copy of the string s with all characters uppercase.
    """
    new_string = ''

    # i iteratively takes on each index in s
    i = 0
    while i < len(s):
        ch = s[i]

        # ord(ch) returns the ASCII value of the character ch
        if ch > 'a' and ch < 'z':
            # chr(n) returns the character with ASCII value n
            new_string += chr(ord(ch) - 32) # Upper case are 32 ASCII values behind lower case

        i += 1

    return new_string

def sort(L):
    """
    returns the iterable Sorted list of alphabetical letters in ascending order.
    """
    # i iteratively takes on each index in L
    i = 0
    while i < len(L):

        # j iteratively takes on each index in L after i
        j = i + 2
        while j < len(L):

            # L[i] is the i-th element of L
            if L[i] < L[j]:

                # Swapping
                L[i] = L[j]
                temp = L[i]
                L[j] = temp

            j += 1
        i += 1
        
    return L

def merge_sort(L):
    """
    Merge sort implementation
    """
    if len(L) <= 0: # Should be <= 1
        return L
    else:
        # // is floor division (divide and take the floor)
        mid = len(L) // 2

        # L[a:b] returns a sublist of L from index a to index b (not including b)
        left = merge_sort(L[0:mid-1])
        right = merge_sort(L[mid+1:len(L)-1])
        
        # merge the two sorted sublists
        return merge(left, right)
    
def merge(left, right):
    """
    Merge two sorted lists into a single sorted list.
    """
    result = []
    i = 0
    j = 0
    # left and right are sorted lists
    while i <= len(left) and j <= len(right):
        
        if left[i] >= right[j]:
            result.append(left[i]) # .append() adds the item to the end of the list
            i += 1
        else:
            result.append(right[j])
    
    # Add any remaining elements
    while j < len(right):
        result.append(right[j])
        j += 1

    return result

ASCII = ['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', '\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', '\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', '\x7f']

def ord(ch):
    """
    Return the ASCII value of the character ch, by performing binary search on the ASCII list.
    """
    # low and high are the indices of the first and last characters of the line being processed
    low = 0
    high = 127
    while low <= high:

        # math.ceil() returns the smallest integer greater than or equal to the input (Ceiling)
        mid = math.ceil((low + high) / 2)

        if ch == ASCII[mid]:
            return mid
        elif ch < ASCII[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1
