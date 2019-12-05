#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:14:34 2019

@author: Mallika Walia & Dasmer Singh
"""

# List of secret santa participants (INPUT LIST)
gifters = [
    "Akshay Kini",
    "Anirban Poddar",
    "Dasmer Singh",
    "Mallika Walia",
    "Ritu Malhotra",
    "Shivam Pappu",
    "Sidd Bhatt",
    "Suchith Vasudevan"
    ]


# Import packages
import base64
from urllib.parse import quote
import random


# Function to convert giftee names to base64 + URL encoded URLs
def secret_santa_url(input_string):
    # Base64 Encoding
    encodedBytes = base64.b64encode(input_string.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")

    # URL Encoding Encoding
    url_b64_encoded_str = quote(encodedStr.encode('utf8'))

    # Append to URL String
    url_string = "https://dasmer.com/secret-santa?p=" + url_b64_encoded_str

    return url_string


def main():
    # Shuffle gifters to create a list of giftees where the name at any index i in
    # both arrays is not the same.
    # (A gifter should never be assigned to be their own secret santa.)
    giftees = []
    gifter_gifts_self = True
    while gifter_gifts_self:

        # Shuffle gifters to create giftee list
        giftees = random.sample(gifters, len(gifters))
        num_non_matching_pairs = 0

        for i in range(0,len(gifters)):
            if gifters[i] != giftees[i]:
                num_non_matching_pairs += 1
            # If each gifter in the input list has a giftee
            # that is NOT themselves, end shuffling
            if num_non_matching_pairs == len(gifters):
                gifter_gifts_self = False


    # Create a list of links to display the giftee's name
    links = []
    for name in giftees:
        links.append(secret_santa_url(name))

    # Print the name of the gifter and their giftee link
    for i in range(0,len(gifters)):
        print(f"{gifters[i]}'s match is {links[i]}")

if __name__ == '__main__':
    main()
