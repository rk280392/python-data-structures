#!/usr/bin/python3

def main() :
    s = input("Enter the string: ").lower()
    s_list = list(s)

    reverse(s_list)
    s_reverse = "".join(s_list)
    if s == s_reverse:
        print(f'{s} is a palindrom')
    else:
        print(f'{s} is not a palindrom')


def reverse(s_list) :
    start_s = 0
    end_s = len(s_list) - 1

    while start_s < end_s:
        s_list[start_s],s_list[end_s] = s_list[end_s], s_list[start_s]
        start_s += 1
        end_s -= 1
    return s_list 



if __name__== "__main__":
    main()
