#! /usr/bin/python
# -*- coding: utf-8 -*-
from gensim.summarization import summarize

def summarizing(article):
    if len(article.split())<=100:
        return article
    return summarize(article,word_count=100)

if __name__=="__main__":
    text = """The SVG <text> element defines a graphics element consisting of text. It's possible to apply a gradient, pattern, clipping path, mask, or filter to <text>, just like any other SVG graphics element."""
    print summarizing(text)
#    aux = ''
#    text = '\n'.join(iter(raw_input,aux))
#    print text
#    print summarizing(text)
