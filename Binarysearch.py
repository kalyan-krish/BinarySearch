# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def Binarysearch(l,search):
    low = 0
    high = len(l)-1
    mid =0
    while low <= high:
        mid = (low+high)//2
        
        if l[mid] < search:
            low = mid+1
        elif l[mid] > search:
            high = mid-1
        else:
            return mid
        
    return -1
    
l = [1,3,4,5,6,7]
search = 3

result = Binarysearch(l,search)

if result ! = -1:
    print(result)

else:
    print('Element not found')


With Recursion:

# Binary Search in python


def binarySearch(array, x, low, high):

    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if array[mid] == x:
            return mid

        # Search the left half
        elif array[mid] > x:
            return binarySearch(array, x, low, mid-1)

        # Search the right half
        else:
            return binarySearch(array, x, mid + 1, high)

    else:
        return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
