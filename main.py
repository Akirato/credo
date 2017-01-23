#!/usr/bin/python3
# Research Center : LTRC, IIIT Hyderabad
__author__ = ["Akirato","revsi"]

from keywy import rake
import golden_retriever as gr
import codecs
debug = True


def main():
    with codecs.open('input.txt', 'r', encoding='utf-8') as myfile:
        text=myfile.read()
    print "============================CREDO============================"
    print "Input Text : "+text
    print "===========================Results===========================\n\n"

    #keywords extraction
    keywords = rake.extract_keywords(text)
    if debug:
        print "===========================Keywords===========================\n"
        print keywords 
        print "\n\n"

    candidate_keywords = ' '.join([i[0] for i in keywords[:min(5,len(keywords))]])

    if debug:
        print "===========================Candidate Keywords===========================\n"
        print candidate_keywords 
        print "\n\n"

    search_results = gr.search(candidate_keywords)

    if debug:
        print "===========================Search Results===========================\n"
        for i in search_results:
            print "===="+i.description+"====="+str(len(i.description))+"\n"
        print "\n\n"

    

    

main()
