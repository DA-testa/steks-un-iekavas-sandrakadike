# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i+1))
            # Process opening bracket, write your code here
            pass

        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return (i+1)
            opening_brackets_stack.pop()
    if  opening_brackets_stack:
        return opening_brackets_stack[0].position
    return ("Success")
            
    # return "Success"
    #print("ir tukss")
    # Process closing bracket, write your code here
    pass
    # if (opening_brackets_stack.len(-1)):
    #     print ("Success")


def main():
    izvele=(input())
    if "I" in izvele:
        text=input("ievadi tekstu: ")
        # if "F" in izvele:
        #     fname=str(input)
        #     text= import (fname.txt)

        
        mismatch = find_mismatch(text)
        print (mismatch)

    # Printing answer, write your code here


if __name__ == "__main__":
    main()

