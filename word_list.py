# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 00:19:34 2016

@author: Sargon
"""

filename = "word_list.txt"
new_words = "new_words.txt"

def word_list(file=filename):
    l = []
    f = open(file, "r")
    for line in f:
        line = line.strip().replace(" ", "")
        l.append(line)
        if len(l) >= 2:
            if l[-1] == l[-2]:
                l = l[:-1]
    f.close()
    #print(l)
    return l

def add_word(l, word):
    l.append(word.strip().lower())
    return l
    
def add_list(l, file=new_words):
    f = open(file, "r")
    for line in f:
        l = add_word(l, line)
    f.close()
    #print(l)
    return l
    
def finish(l):
    l.sort()
    f = open(filename, "w")
    for word in l:
        if word != "\n":
            f.write(word + "\n")
    f.close()
    
if __name__ == "__main__":
    l = word_list()
    l = add_list(l)
    finish(l)
        
    
        
    