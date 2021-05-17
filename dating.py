#!/usr/bin/env python3
# Created by: Jonathan Kene
# Created on: May. 17, 2021
# This program allows the user enters their age
# and then the program tells the user if they can date the
# grandparent's grandchild or not.

def main():

    # asks the user to type their age
    print("Grandparent #1  will only approve of you dating their grandchild"
          " if you are older than 25 AND younger than 40.")
    # get the user's guess
    user_age_string = input("Enter your age: ")
    print("")

    # make sure if the user types anything but an integer, it's not valid
    try:
        user_age_int = int(user_age_string)
        print("")
    except ValueError:
        print("{} is not a number" .format(user_age_string))

    else:
        # check if the age is above 20 and below 40s
        if user_age_int > 25 and user_age_int < 40:
            print("You can date the grandchild")
        elif user_age_int < 25:
            print("I'm sorry but your too young to date the grandchild")
        elif user_age_int > 40:
            print("I'm sorry but your too old to date the grandchild")
    finally:
        print("")
        print("Thank you for your input")


if __name__ == "__main__":
    main()
