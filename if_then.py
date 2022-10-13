#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Oct 2022
# This program is a number choosing game

import constants


def main():
    # this function sees if you've chosen the right number

    # input
    user_number = int(input("Pick a number between 0-9: "))

    # process
    if user_number == constants.CHOSEN_NUMBER:
        # output
        print("You've chosen the right number! Good job.")

    if user_number != constants.CHOSEN_NUMBER:
        # output
        print("That's not the right number, try again!")

    print("")
    print("\nDone.")


if __name__ == "__main__":
    main()
