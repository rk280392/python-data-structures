#!/usr/bin/python3


import nameScript as ns
ns.myFunction()

def mySecondFunction():
    print (f'The value of __name__ is {__name__}')

def main():
    mySecondFunction()

if __name__ == '__main__':
    main()
