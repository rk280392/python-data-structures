#!/usr/bin/python3


def main() :

    mlist = []
    n = int(input("Enter the number of elements needed: "))

    for num in range(0,n):
        ele = int(input())
        mlist.append(ele)

    reverse(mlist)
    print(f"reversed list is { mlist }")


def reverse(mlist):

    start_index = 0
    end_index = len(mlist) - 1

    while start_index < end_index:
        mlist[start_index], mlist[end_index] = mlist[end_index], mlist[start_index]
        start_index += 1
        end_index -= 1

if __name__ == "__main__":
    main()

