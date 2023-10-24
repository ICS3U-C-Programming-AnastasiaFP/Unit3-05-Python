#!/usr/bin/env python3
# Created by: Anastasia Friedenstein Patino
# Created on: October. 20, 2023
# Month from integer game


def main():
    user_integer = int(input("Enter an integer:"))

    match user_integer:
        case 1:
            print("1 is January")
        case 2:
            print("2 is February")
        case 3:
            print("3 is March")
        case 4:
            print("4 is April")
        case 5:
            print("5 is May")
        case 6:
            print("6 is June")
        case 7:
            print("7 is July")
        case 8:
            print("8 is August")
        case 9:
            print("9 is September")
        case 10:
            print("10 is October")
        case 11:
            print("11 is November")
        case 12:
            print("12 is December")
        case _:
            print("Error")


if __name__ == "__main__":
    main()
