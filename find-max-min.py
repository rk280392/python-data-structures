#!/usr/bin/python3


def main() :

    mlist = []
    n = int(input("Enter number of elements : "))
    for i in range(0,n):
        element = int(input())
        mlist.append(element)
    max_value = find_max(mlist)
    
    print(f"Max value is: { max_value }")

    min_value = find_min(mlist)
    print(f"Min value is: { min_value }")


def find_max(mlist):
    max_val = mlist[0]
    for num in mlist:
        if num > max_val:
            max_val = num
    return max_val

def find_min(mlist):
    min_val = mlist[0]
    for num in mlist:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == "__main__":
    main()
