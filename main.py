#!/usr/bin/python3
# Research Center : LTRC, IIIT Hyderabad
__author__ = ["Akirato","revsi"]

from keywy import rake
debug = True
def main():
    with open('input.txt', 'r') as myfile:
        text=myfile.read()
    print "============================CREDO============================"
    print "Input Text : "+text
    print "===========================Results===========================\n\n"

    #keywords extraction
    keywords = rake.extract_keywords(text)
    if debug:
        print "===========================Keywords===========================\n\n"
        print keywords

    

    

main()
